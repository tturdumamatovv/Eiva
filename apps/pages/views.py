from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import WelcomePage, MainPage, AboutPage, ContactInformation
from .serializers import WelcomePageSerializer, MainPageSerializer, AboutPageSerializer, ContactInformationSerializer


# Create your views here.


class WelcomePageAPIView(APIView):
    def get(self, request, *args, **kwargs):
        welcome = WelcomePage.objects.first()
        if not welcome:
            welcome = WelcomePage.objects.create(
                title='Клиника ЭЙВА',
                description='Внимание и забота на каждом этапе',
                text_button='Записаться на прием',
                link_button='#',
            )
            serializer = WelcomePageSerializer(welcome)
            return Response(serializer.data)

        serializer = WelcomePageSerializer(welcome)
        return Response(serializer.data)


class MainPageAPIView(APIView):
    def get(self, request, *args, **kwargs):
        welcome = MainPage.objects.first()
        if not welcome:
            welcome = MainPage.objects.create(
                our_services_title='Направления деятельности',
                our_specialists_title='Наши специалисты',
                about_us_title='О нас',
                about_us_description='',
                counter_title='Счетчик рождения',
                counter_sub_title='У нас родилось 1 000 малышей!',
                birth_counter=1000,
                birth_counter_sub_title='малышей родилось с 2020 г.',
                boys_counter='500',
                girls_counter='500',
            )
            serializer = MainPageSerializer(welcome)
            return Response(serializer.data)

        serializer = MainPageSerializer(welcome)
        return Response(serializer.data)


class AboutPageAPIView(APIView):
    def get(self, request, *args, **kwargs):
        about_page = AboutPage.objects.first()
        if not about_page:
            about_page = AboutPage.objects.create(
                title='О нас',
                text='',
                image=None,
                counter_1_title='Количество событий',
                counter_1_value=100,
                counter_2_title='Количество публикаций',
                counter_2_value=150,
                counter_3_title='Количество проектов',
                counter_3_value=200,
                cards_title='Наши услуги',
                faq_title='Часто задаваемые вопросы',
                partners_title='Наши партнеры',
                gallery_title='Галерея',
            )
        serializer = AboutPageSerializer(about_page)
        return Response(serializer.data)

class ContactInformationView(APIView):
    def get(self, request, *args, **kwargs):
        contact_info = ContactInformation.objects.first()
        if not contact_info:
            return Response({'error': 'Контактная информация не найдена'}, status=404)
        serializer = ContactInformationSerializer(contact_info)
        return Response(serializer.data)