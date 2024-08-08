from django.contrib import admin
from .models import Service, Package, Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', ]
    search_fields = ['name', ]
    list_filter = ['name']


class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'description']
    search_fields = ['name', 'description']
    list_filter = ['category', 'price']


class PackageAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'description']
    filter_horizontal = ['services']  # Удобный способ выбора услуг для пакета
    search_fields = ['name', 'description']
    list_filter = ['price']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Package, PackageAdmin)
