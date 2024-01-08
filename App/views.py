from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import Plant
from .serializers import PlantSerializer


class PlantViewSet(ModelViewSet):
    queryset = Plant.objects.all()
    serializer_class = PlantSerializer
    parser_classes = (MultiPartParser, FormParser)
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filter_fields = ['price']
    search_fields = ['text']
    ordering_fields = ['price']

    def create(self, request, *args, **kwargs):
        text = request.data["text"]
        price = request.data["price"]
        picture = request.data["picture"]

        Plant.objects.create(text=text, price=price, picture=picture)
        return Response("Plant created successfully", status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.delete()

# Create your views here.
