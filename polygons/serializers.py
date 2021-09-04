from rest_framework import serializers

from .models import ProviderServiceArea
from providers.models import Provider


class ProviderServiceAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProviderServiceArea
        fields = ('id', 'provider', 'name', 'price', 'polygon')

    def to_internal_value(self, data):
        if "provider" in data:
            provider = Provider.objects.filter(name=data["provider"])
            if not provider.exists():
                error = {'message': "No Such Provider Found"}
                raise serializers.ValidationError(error)
            data["provider"] = provider.values()[0]["id"]
        return super(ProviderServiceAreaSerializer, self).to_internal_value(data)