from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import WelcomePage
from .serializers import WelcomePageSerializer


# Create your views here.


class WelcomePageView(APIView):
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

