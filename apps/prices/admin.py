from django.contrib import admin
from unfold.admin import ModelAdmin

from .models import Service, Category, Packages, PackageService


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
    pass


@admin.register(PackageService)
class PackageServiceAdmin(ModelAdmin):
    pass
