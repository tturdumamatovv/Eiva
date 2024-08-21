from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Category
from .serializers import CategorySerializer, CategoryListSerializer


class CategoryListAPIView(APIView):
    def get(self, request, *args, **kwargs):
        categories = Category.objects.all()

        serializer = CategoryListSerializer(categories, many=True, context={'request': self.request})
        return Response(serializer.data)


class CategoryAPIView(APIView):
    def get(self, request, *args, **kwargs):
        categories = Category.objects.get(id=self.kwargs['pk'])

        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data, context={'request': self.request})