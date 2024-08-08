from django.contrib import admin
from .models import Category, Type, Service, ServiceItem


class ServiceItemInline(admin.TabularInline):
    model = ServiceItem
    extra = 0  # Указывает, сколько пустых форм для новых записей отображать по умолчанию


class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'type']  # Поля, которые будут отображаться в списке объектов
    inlines = [ServiceItemInline]  # Добавление вложенных элементов услуги


class TypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'subtitle']
    # inlines = [ServiceAdmin]  # Так как ServiceAdmin не является inline, этот параметр недопустим здесь


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'title', 'description']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Type, TypeAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(ServiceItem)  # Если нужно управлять элементами независимо, можно зарегистрировать отдельно
