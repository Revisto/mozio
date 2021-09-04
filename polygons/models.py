from django.db import models


# Create your models here.


class ProviderServiceArea(models.Model):
    provider = models.ForeignKey('providers.Provider', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    price = models.FloatField()
    polygon = models.JSONField()

    def __str__(self):
        return self.name
