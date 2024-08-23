from rest_framework import serializers
from .models import Category, Type, Service, ServiceItem


class ServiceItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceItem
        fields = ('text', 'image', 'image_duration')


class ServiceSerializer(serializers.ModelSerializer):
    items = ServiceItemSerializer(many=True, source='serviceitem_set')  # используем related_name если он установлен

    class Meta:
        model = Service
        fields = ('title', 'items')


class TypeSerializer(serializers.ModelSerializer):
    services = ServiceSerializer(many=True, source='service_set')  # используем related_name если он установлен

    class Meta:
        model = Type
        fields = ('title', 'subtitle', 'services')


class CategorySerializer(serializers.ModelSerializer):
    types = TypeSerializer(many=True, source='type_set')

    class Meta:
        model = Category
        fields = ('name', 'types')


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('slug', 'description', 'name', 'icon')
