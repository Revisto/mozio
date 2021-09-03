from django.db import models


# Create your models here.
class Provider(models.Model):
    name = models.CharField("name", max_length=255)
    email = models.EmailField(max_length=255)
    phone_number = models.IntegerField("phone")
    language = models.CharField("language", max_length=255)
    currency = models.CharField("currency", max_length=10)

    def __str__(self):
        return self.name


class ProviderServiceArea(models.Model):
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    price = models.FloatField()
    polygon = models.JSONField()

    def __str__(self):
        return self.name
