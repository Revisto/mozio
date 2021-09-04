from rest_framework import viewsets

from .serializers import ProviderSerializer
from .models import Provider


class ProviderViewSet(viewsets.ModelViewSet):
    queryset = Provider.objects.all().order_by('name')
    serializer_class = ProviderSerializer