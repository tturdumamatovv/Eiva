from django.contrib import admin
from unfold.admin import ModelAdmin, StackedInline

from .models import (WelcomePage, Advantages, MainPage, AboutPage, AboutCard, AboutFAQ,
                     AboutFAQImage, AboutPartners, AboutGallery, Email, SocialNetwork, PhoneNumber, Documents, Document,
                     ContactInformation, AboutImages)


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
    extra = 0
    tab = True


@admin.register(AboutPartners)
class AboutPartnersInline(ModelAdmin):
    pass


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
    extra = 0


@admin.register(Documents)
class DocumentsAdmin(ModelAdmin):
    inlines = [DocumentAdmin]


@admin.register(MainPage)
class MainPageAdmin(ModelAdmin):
    pass
