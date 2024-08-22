from django.contrib import admin
from .models import Service, Category, Packages,PackageService


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', ]
    search_fields = ['name', ]
    list_filter = ['name']


class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']
    search_fields = ['name', 'description']
    list_filter = ['category', 'price']


class PackageAdmin(admin.ModelAdmin):
    pass

@admin.register(PackageService)
class PackageServiceAdmin(admin.ModelAdmin):
    pass

admin.site.register(Category, CategoryAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Packages, PackageAdmin)
