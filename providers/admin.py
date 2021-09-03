from django.contrib import admin
from .models import Provider, ProviderServiceArea

# Register your models here.
admin.site.register(Provider)
admin.site.register(ProviderServiceArea)