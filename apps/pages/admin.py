from django.contrib import admin
from django.db import models
from unfold.admin import ModelAdmin, StackedInline
from unfold.contrib.forms.widgets import WysiwygWidget


from .models import (
    FormBackgroundImage,
    WelcomePage,
    Advantages,
    MainPage,
    AboutPage,
    AboutCard,
    AboutFAQ,
    AboutFAQImage,
    AboutPartners,
    AboutGallery,
    Email,
    SocialNetwork,
    PhoneNumber,
    Documents,
    Document,
    ContactInformation,
    AboutImages,
    MetaData, SiteSettings,
)


class AdvantagesInline(StackedInline):
    model = Advantages
    extra = 0
    tab = True


@admin.register(WelcomePage)
class WelcomePageAdmin(ModelAdmin):
    inlines = [AdvantagesInline]


class AboutCardInline(StackedInline):
    model = AboutCard
    extra = 0
    tab = True


class AboutFAQImageInline(StackedInline):
    model = AboutFAQImage
    extra = 0
    tab = True


class AboutFAQInline(StackedInline):
    model = AboutFAQ
    extra = 0
    tab = True


class AboutGalleryInline(StackedInline):
    model = AboutGallery
    extra = 0
    tab = True


@admin.register(AboutPage)
class AboutPageAdmin(ModelAdmin):
    inlines = [AboutCardInline, AboutGalleryInline, AboutFAQInline, AboutFAQImageInline]


class AboutImagesInline(StackedInline):
    model = AboutImages
    extra = 1
    tab = True


@admin.register(AboutPartners)
class AboutPartnersInline(ModelAdmin):
    inlines = [AboutImagesInline]


class PhoneNumberAdmin(StackedInline):
    model = PhoneNumber
    extra = 0


class SocialNetworkAdmin(StackedInline):
    model = SocialNetwork
    extra = 0


class EmailAdmin(StackedInline):
    model = Email
    extra = 0


@admin.register(ContactInformation)
class ContactInformationAdmin(ModelAdmin):
    inlines = [PhoneNumberAdmin, SocialNetworkAdmin, EmailAdmin]


class DocumentAdmin(StackedInline):
    model = Document
    extra = 1
    formfield_overrides = {
        models.TextField: {
            "widget": WysiwygWidget,
        },
    }


@admin.register(Documents)
class DocumentsAdmin(ModelAdmin):
    inlines = [DocumentAdmin]


@admin.register(MainPage)
class MainPageAdmin(ModelAdmin):
    pass


@admin.register(MetaData)
class MetaDataAdmin(ModelAdmin):
    pass


@admin.register(FormBackgroundImage)
class FormBackgroundImageAdmin(ModelAdmin):
    pass


@admin.register(SiteSettings)
class SiteSettingsAdmin(ModelAdmin):
    pass