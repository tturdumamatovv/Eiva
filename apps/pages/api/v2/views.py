from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import (
    MainPageOurServicesSerializer,
    MainPageOurSpecialistsSerializer,
    MainPageAboutUsSerializer,
    MainPageBirthCounterSerializer,
    MainPageContactsSerializer,
    AboutPageAboutUsSerializer,
    AboutPageIncludeSerializer,
    AboutPageFAQSerializer,
    AboutPageParentsSerializer,
    AboutPageGallerySerializer,
)
from ...models import AboutPage, MainPage


class MainPageOurServicesAPIView(APIView):
    def get(self, obj):
        serializer = MainPageOurServicesSerializer(context={'request': self.request})
        return Response(serializer.data)


class MainPageOurSpecialistsAPIView(APIView):
    def get(self, obj):
        serializer = MainPageOurSpecialistsSerializer(context={'request': self.request})
        return Response(serializer.data)


class MainPageAboutUsAPIView(APIView):
    def get(self, obj):
        obj = MainPage.objects.first()
        serializer = MainPageAboutUsSerializer(obj, context={'request': self.request})
        return Response(serializer.data)


class MainPageBirthCounterAPIView(APIView):
    def get(self, obj):
        obj = MainPage.objects.first()
        serializer = MainPageBirthCounterSerializer(obj, context={'request': self.request})
        return Response(serializer.data)


class MainPageContactsAPIView(APIView):
    def get(self, obj):
        # MainPageContactsSerializer
        pass


# ABUT PAGE

class AboutPageAboutUsAPIView(APIView):
    def get(self, obj):
        obj = AboutPage.objects.first()
        serilizer = AboutPageAboutUsSerializer(obj, context={'request': self.request})
        return Response(serilizer.data)


class AboutPageIncludeAPIView(APIView):
    def get(self, obj):
        obj = AboutPage.objects.first()
        serilizer = AboutPageIncludeSerializer(obj, context={'request': self.request})
        return Response(serilizer.data)


class AboutPageFAQAPIView(APIView):
    def get(self, obj):
        obj = AboutPage.objects.first()
        serilizer = AboutPageFAQSerializer(obj, context={'request': self.request})
        return Response(serilizer.data)


class AboutPageParentsAPIView(APIView):
    def get(self, obj):
        obj = AboutPage.objects.first()
        serilizer = AboutPageParentsSerializer(obj, context={'request': self.request})
        return Response(serilizer.data)


class AboutPageGalleryAPIView(APIView):
    def get(self, obj):
        obj = AboutPage.objects.first()
        serilizer = AboutPageGallerySerializer(obj, context={'request': self.request})
        return Response(serilizer.data)
