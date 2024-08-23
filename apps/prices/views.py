from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Service, Packages, Category, PackageService, PackageServiceType
from .serializers import ServiceSerializer, PackageSerializer, CategorySerializer, PackageServicesSerializer, \
    PackageServicesTypeSerializer, PreiskurantSerializer


class CategoryListView(APIView):
    def get(self, request, *args, **kwargs):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True, context={'request': self.request})
        return Response(serializer.data)


class ServiceListView(APIView):
    def get(self, request, *args, **kwargs):
        services = Service.objects.filter(category=self.kwargs['category_id'])
        serializer = ServiceSerializer(services, many=True, context={'request': self.request})
        return Response(serializer.data)


class PackageListView(APIView):
    def get(self, request, *args, **kwargs):
        packages = Packages.objects.first()
        if not packages:
            packages = Packages.objects.create(
                name_standard='Стандарт',
                name_comfort='Комфорт',
                name_vip='VIP',
            )
        serializer = PackageSerializer(packages, many=False, context={'request': self.request})
        return Response(serializer.data)


class PackageServicesTypeListView(APIView):
    def get(self, obj):
        package_service = PackageServiceType.objects.all()
        serializer = PackageServicesTypeSerializer(package_service, many=True, context={'request': self.request})
        return Response(serializer.data)

class PreiskurantAPIView(APIView):
    def get(self, request, *args, **kwargs):
        packeges = Packages.objects.all()
        serializer = PreiskurantSerializer(packeges, many=True, context={'request': self.request})
        return Response(serializer.data)


