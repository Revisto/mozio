from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response


from .serializers import ProviderServiceAreaSerializer
from .models import ProviderServiceArea
from .validators import Polygons

class ProviderServiceAreaViewSet(viewsets.ModelViewSet):
    queryset = ProviderServiceArea.objects.all().order_by('name')
    serializer_class = ProviderServiceAreaSerializer

class PolygonsPoint(APIView):

    def get(self, request):
        is_valid = Polygons().polygons_point_validator(request)
        if is_valid is not True:
            return Response(is_valid)

        data = request.data
        polygons = ProviderServiceArea.objects.all()
        serializer = ProviderServiceAreaSerializer(polygons, many=True)
        list_of_polygons = []
        for polygon in serializer.data:
            coordinates = polygon["polygon"]["coordinates"][0]
            for coordinate in coordinates:
                if float(coordinate[0]) == float(data["lat"]) and float(coordinate[1]) == float(data["lon"]):
                    match = {
                        "name": polygon["name"],
                        "price": polygon["price"],
                        "provider_id": polygon["provider"],
                    }
                    list_of_polygons.append(match)
                    break
        return Response(list_of_polygons)