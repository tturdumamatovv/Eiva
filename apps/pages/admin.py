from django.contrib import admin

# Register your models here.

from django.contrib import admin
import nested_admin
from .models import (WelcomePage, Advantages, MainPage, AboutPage, AboutCard, AboutFAQ,
                     AboutFAQImage, AboutPartners, AboutGallery)


class AdvantagesInline(nested_admin.NestedTabularInline):
    model = Advantages
    extra = 0


class WelcomePageAdmin(nested_admin.NestedModelAdmin):
    inlines = [AdvantagesInline]


class AboutCardInline(nested_admin.NestedTabularInline):
    model = AboutCard
    extra = 0


class AboutFAQImageInline(nested_admin.NestedTabularInline):
    model = AboutFAQImage
    extra = 0


class AboutFAQInline(nested_admin.NestedTabularInline):
    model = AboutFAQ
    extra = 0


class AboutPartnersInline(nested_admin.NestedTabularInline):
    model = AboutPartners
    extra = 0


class AboutGalleryInline(nested_admin.NestedTabularInline):
    model = AboutGallery
    extra = 0


class AboutPageAdmin(nested_admin.NestedModelAdmin):
    inlines = [AboutCardInline, AboutPartnersInline, AboutGalleryInline, AboutFAQInline, AboutFAQImageInline]


admin.site.register(WelcomePage, WelcomePageAdmin)
admin.site.register(MainPage)
admin.site.register(AboutPage, AboutPageAdmin)
