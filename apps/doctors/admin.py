from adminsortable2.admin import SortableAdminMixin
from django.contrib import admin
from .models import Position, Specialization, Doctor, Сertificate, Review, Photo, Order
from unfold.admin import ModelAdmin, TabularInline



class CertificateInline(TabularInline):
    model = Сertificate
    extra = 1  # Количество форм для новых записей


class ReviewInline(TabularInline):
    model = Review
    extra = 1


class PhotoInline(TabularInline):
    model = Photo
    extra = 1


@admin.register(Doctor)
class DoctorAdmin(SortableAdminMixin, ModelAdmin):
    # for docktor in Doctor.objects.all():
    #     docktor.order = docktor.id
    #     docktor.save()
    inlines = [CertificateInline, ReviewInline, PhotoInline]
    list_display = ('name', 'position', 'specialization', 'seniority')  # Какие поля показывать в списке
    search_fields = ('name',)  # Поля, по которым можно осуществлять поиск


@admin.register(Position)
class PositionAdmin(ModelAdmin):
    pass


@admin.register(Specialization)
class SpecializationAdmin(ModelAdmin):
    pass


@admin.register(Order)
class OrderAdmin(ModelAdmin):
    pass
# admin.site.register(Сertificate)
# admin.site.register(Review)
# admin.site.register(Photo)
