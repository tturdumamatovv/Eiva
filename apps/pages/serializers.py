from rest_framework import serializers

from .models import WelcomePage, Advantages


class AdvantagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advantages
        fields = ['text', 'icon', ]


class WelcomePageSerializer(serializers.ModelSerializer):
    advantages = AdvantagesSerializer(many=True, read_only=True)

    class Meta:
        model = WelcomePage
        fields = ['image', 'title', 'description', 'text_button', 'link_button', 'advantages', ]
