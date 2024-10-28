from django.contrib import admin
from .models import Category, Type, Service, ServiceItem
from unfold.admin import ModelAdmin, TabularInline
from adminsortable2.admin import SortableAdminMixin


class ServiceItemInline(TabularInline):
    model = ServiceItem
    extra = 0
    tab = True



@admin.register(Service)
class ServiceAdmin(ModelAdmin):
    list_display = ['title', 'type']  # Поля, которые будут отображаться в списке объектов
    list_filter = ['type']
    inlines = [ServiceItemInline]  # Добавление вложенных элементов услуги


@admin.register(Type)
class TypeAdmin(ModelAdmin):
    list_display = ['name', 'category', 'subtitle']
    list_filter = ['category']
    # inlines = [ServiceAdmin]  # Так как ServiceAdmin не является inline, этот параметр недопустим здесь


@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    list_display = ['name', 'title', 'description']


@admin.register(ServiceItem)
class ServiceItemAdmin(SortableAdminMixin, ModelAdmin):
    list_display = ['text', 'service']
    list_filter = ['service']
