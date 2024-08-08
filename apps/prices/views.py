from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Service, Package, Category
from .serializers import ServiceSerializer, PackageSerializer, CategorySerializer


class CategoryListView(APIView):
    def get(self, request, *args, **kwargs):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)


class ServiceListView(APIView):
    def get(self, request, *args, **kwargs):
        services = Service.objects.filter(category=self.kwargs['category_id'])
        serializer = ServiceSerializer(services, many=True)
        return Response(serializer.data)


class PackageListView(APIView):
    def get(self, request, *args, **kwargs):
        packages = Package.objects.prefetch_related('services').all()
        serializer = PackageSerializer(packages, many=True)
        return Response(serializer.data)
