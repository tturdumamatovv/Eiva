from django.contrib import admin
from .models import Position, Specialization, Doctor, Сertificate, Review, Photo


class CertificateInline(admin.TabularInline):
    model = Сertificate
    extra = 1  # Количество форм для новых записей


class ReviewInline(admin.TabularInline):
    model = Review
    extra = 1


class PhotoInline(admin.TabularInline):
    model = Photo
    extra = 1


class DoctorAdmin(admin.ModelAdmin):
    inlines = [CertificateInline, ReviewInline, PhotoInline]
    list_display = ('name', 'position', 'specialization', 'seniority')  # Какие поля показывать в списке
    search_fields = ('name',)  # Поля, по которым можно осуществлять поиск


admin.site.register(Position)
admin.site.register(Specialization)
admin.site.register(Doctor, DoctorAdmin)
# admin.site.register(Сertificate)
# admin.site.register(Review)
# admin.site.register(Photo)
