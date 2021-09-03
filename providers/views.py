from rest_framework import viewsets

from .serializers import ProviderSerializer, ProviderServiceAreaSerializer
from .models import Provider, ProviderServiceArea


class ProviderViewSet(viewsets.ModelViewSet):
    queryset = Provider.objects.all().order_by('name')
    serializer_class = ProviderSerializer

class ProviderServiceAreaViewSet(viewsets.ModelViewSet):
    queryset = ProviderServiceArea.objects.all().order_by('name')
    serializer_class = ProviderServiceAreaSerializer