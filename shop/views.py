from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from .serializers import CategorySerializer, ProductSerializer
from shop.models import Category, Product


class CategoryViewset(ReadOnlyModelViewSet):
    
    serializer_class = CategorySerializer
    
    def get_queryset(self):
        return Category.objects.all()

