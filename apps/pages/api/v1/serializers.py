from rest_framework import serializers

from apps.doctors.models import Doctor
from apps.doctors.serializers import DoctorListSerializer
from apps.pages.models import WelcomePage, Advantages, MainPage, AboutPage, ContactInformation, SocialNetwork, Email, \
    PhoneNumber, \
    AboutCard, AboutFAQ, AboutFAQImage, AboutPartners, AboutGallery, AboutImages
from apps.prices.models import Category as PriceCategory
from apps.prices.serializers import CategorySerializer as PriceCategorySerializer


class AdvantagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advantages
        fields = ['text', 'icon', ]


class WelcomePageSerializer(serializers.ModelSerializer):
    advantages = AdvantagesSerializer(many=True, read_only=True)

    class Meta:
        model = WelcomePage
        fields = ['image', 'title', 'description', 'text_button', 'link_button', 'advantages', ]


class MainPageSerializer(serializers.ModelSerializer):
    our_services = serializers.SerializerMethodField(read_only=True)
    our_specialists = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = MainPage
        fields = [
            'our_services_title',
            'our_services',
            'our_specialists_title',
            'about_us_title',
            'about_us_description',
            'counter_title',
            'counter_sub_title',
            'birth_counter',
            'birth_counter_sub_title',
            'boys_counter',
            'girls_counter',
        ]

    def get_our_services(self):
        obj = PriceCategory.objects.all()
        return PriceCategorySerializer(obj, many=True).data

    def ger_our_specialists(self):
        obj = Doctor.objects.all()
        return DoctorListSerializer(obj, many=True).data


class AboutCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutCard
        fields = '__all__'


class AboutFAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutFAQ
        fields = '__all__'


class AboutFAQImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutFAQImage
        fields = '__all__'


class AboutPartnersSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutPartners
        fields = '__all__'

class AboutImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutImages
        fields = '__all__'

class AboutGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutGallery
        fields = '__all__'


class AboutPageSerializer(serializers.ModelSerializer):
    cards = serializers.SerializerMethodField()
    faqs = serializers.SerializerMethodField()
    faq_images = serializers.SerializerMethodField()
    partners = serializers.SerializerMethodField()
    images = serializers.SerializerMethodField()
    gallery = serializers.SerializerMethodField()

    class Meta:
        model = AboutPage
        fields = [
            'title',
            'text',
            'image',
            'counter_1_title',
            'counter_1_value',
            'counter_2_title',
            'counter_2_value',
            'counter_3_title',
            'counter_3_value',
            'cards_title',
            'cards',
            'faq_title',
            'faqs',
            'faq_images',
            'partners_title',
            'partners',
            'gallery_title',
            'gallery',
        ]

    def get_cards(self, obj):
        cards = AboutCard.objects.all()
        return AboutCardSerializer(cards, many=True).data

    def get_faqs(self, obj):
        faqs = AboutFAQ.objects.all()
        return AboutFAQSerializer(faqs, many=True).data

    def get_faq_images(self, obj):
        faq_images = AboutFAQImage.objects.all()
        return AboutFAQImageSerializer(faq_images, many=True).data

    def get_partners(self, obj):
        partners = AboutPartners.objects.all()
        return AboutPartnersSerializer(partners, many=True).data

    def get_images(self, obj):
        images = AboutImages.objects.all()
        return AboutImagesSerializer(images, many=True).data

    def get_gallery(self, obj):
        gallery = AboutGallery.objects.all()
        return AboutGallerySerializer(gallery, many=True).data


class PhoneNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhoneNumber
        fields = ['number']


class EmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = ['email']


class SocialNetworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialNetwork
        fields = ['name', 'url', 'icon']


class ContactInformationSerializer(serializers.ModelSerializer):
    phone_numbers = PhoneNumberSerializer(many=True, read_only=True)
    emails = EmailSerializer(many=True, read_only=True)
    social_networks = SocialNetworkSerializer(many=True, read_only=True)

    class Meta:
        model = ContactInformation
        fields = ['address', 'working_hours_weekdays', 'working_hours_weekend', 'email', 'iframe_map', 'phone_numbers',
                  'emails', 'social_networks']
