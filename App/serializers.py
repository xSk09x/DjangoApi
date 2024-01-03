from rest_framework.serializers import ModelSerializer
from .models import Plant


class PlantSerializer(ModelSerializer):
    class Meta:
        model = Plant
        fields = ["id", "text", "price", "picture"]
