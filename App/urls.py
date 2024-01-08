from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register(r'plants', views.PlantViewSet, basename='plant')


urlpatterns = [
    path('api/', include(router.urls)),
]