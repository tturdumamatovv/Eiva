from rest_framework import serializers

from .models import WelcomePage, Advantages, MainPage, AboutPage


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
    class Meta:
        model = MainPage
        fields = '__all__'


class AboutPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutPage
        fields = '__all__'
