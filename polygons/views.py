from rest_framework import viewsets

from .serializers import ProviderServiceAreaSerializer
from .models import ProviderServiceArea


class ProviderServiceAreaViewSet(viewsets.ModelViewSet):
    queryset = ProviderServiceArea.objects.all().order_by('name')
    serializer_class = ProviderServiceAreaSerializer