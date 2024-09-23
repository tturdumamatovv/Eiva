from django.contrib import admin
from unfold.admin import ModelAdmin

from .models import Service, Category, Packages, PackageService, PackageServiceType


@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    list_display = ['name', ]
    search_fields = ['name', ]
    list_filter = ['name']


@admin.register(Service)
class ServiceAdmin(ModelAdmin):
    list_display = ['name', 'price', 'category']
    search_fields = ['name', 'description']
    list_filter = ['category', 'price']


@admin.register(Packages)
class PackageAdmin(ModelAdmin):
    list_display = ['name_standard', 'standard_is_active', 'comfort_is_active', 'vip_is_active']
    list_filter = ['standard_is_active', 'comfort_is_active', 'vip_is_active']


@admin.register(PackageService)
class PackageServiceAdmin(ModelAdmin):
    list_display = [
        'type',
        'name',
        'price',
        'price_comfort',
        'available_in_comfort',
        'price_vip',
        'available_in_vip',
    ]
    list_filter = ['type', 'available_in_comfort', 'available_in_vip',]


@admin.register(PackageServiceType)
class PackageServiceTypeAdmin(ModelAdmin):
    list_display = ['name', 'package',]
    list_filter = ['package',]

