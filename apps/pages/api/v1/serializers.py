from rest_framework import serializers

from apps.doctors.models import Doctor
from apps.doctors.serializers import DoctorListSerializer
from apps.pages.models import WelcomePage, Advantages, MainPage, AboutPage, ContactInformation, SocialNetwork, Email, \
    PhoneNumber, \
    AboutCard, AboutFAQ, AboutFAQImage, AboutPartners, AboutGallery, AboutImages, Documents, Document
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
            'our_specialists',
            'about_us_title',
            'about_us_description',
            'about_us_image',
            'counter_title',
            'counter_sub_title',
            'birth_counter',
            'birth_counter_sub_title',
            'boys_counter',
            'girls_counter',
        ]

    def get_our_services(self, obj):
        obj = PriceCategory.objects.all()
        return PriceCategorySerializer(obj, many=True, context={'request': self.context.get('request')}).data

    def get_our_specialists(self, obj):
        obj = Doctor.objects.all()
        return DoctorListSerializer(obj, many=True, context={'request': self.context.get('request')}).data


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
    images = serializers.SerializerMethodField()

    class Meta:
        model = AboutPartners
        fields = '__all__'

    def get_images(self, obj):
        images = AboutImages.objects.filter(partner=obj)
        return AboutImagesSerializer(images, many=True, context={'request': self.context.get('request')}).data


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
        request = self.context.get('request')

        cards = AboutCard.objects.all()
        return AboutCardSerializer(cards, many=True, context={'request': request}).data

    def get_faqs(self, obj):
        request = self.context.get('request')

        faqs = AboutFAQ.objects.all()
        return AboutFAQSerializer(faqs, many=True, context={'request': request}).data

    def get_faq_images(self, obj):
        request = self.context.get('request')

        faq_images = AboutFAQImage.objects.all()
        return AboutFAQImageSerializer(faq_images, many=True, context={'request': request}).data

    def get_partners(self, obj):
        request = self.context.get('request')

        partners = AboutPartners.objects.all()
        return AboutPartnersSerializer(partners, many=True, context={'request': request}).data

    def get_gallery(self, obj):
        request = self.context.get('request')
        gallery = AboutGallery.objects.all()
        return AboutGallerySerializer(gallery, many=True, context={'request': request}).data


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


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ['name', 'text', 'file']

class DocumentsSerializer(serializers.ModelSerializer):
    document = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Documents
        fields = '__all__'
    def get_document(self, obj):
        request = self.context.get('request')
        obj = Document.objects.all()
        return DocumentSerializer(obj, many=True, context={'request': request} ).data


class ContactInformationSerializer(serializers.ModelSerializer):
    phone_numbers = PhoneNumberSerializer(many=True, read_only=True)
    emails = EmailSerializer(many=True, read_only=True)
    social_networks = SocialNetworkSerializer(many=True, read_only=True)

    class Meta:
        model = ContactInformation
        fields = '__all__'
