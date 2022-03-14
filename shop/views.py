from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import CategorySerializer, ProductSerializer
from shop.models import Category, Product



class CategoryAPIView(APIView):
    
    def get(self, *arg, **kwargs):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)
    
class ProductAPIView(APIView):
    
    def get(self, *args, **kwargs):
        
        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)