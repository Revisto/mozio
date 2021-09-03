from rest_framework import serializers

from .models import Provider, ProviderServiceArea

class ProviderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Provider
        fields = ('name', 'email', 'phone_number', 'language', 'currency')