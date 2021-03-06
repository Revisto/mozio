from django.urls import include, path
from rest_framework import routers


from . import views

router = routers.DefaultRouter()
router.register(r'polygons', views.ProviderServiceAreaViewSet)

# Wire up our API using automatic URL routing.
urlpatterns = [
    path('', include(router.urls)),
    path('polygon-point', views.PolygonsPoint.as_view()),
]