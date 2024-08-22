from rest_framework import serializers
from .models import Service, Packages, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id', 'name', 'price']


class PackageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Packages
        fields = '__all__'


class PackageServicesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Service
        fields = '__all__'
