from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Doctor
from .send_telegram_message import send_telegram_message
from .serializers import DoctorListSerializer, DoctorDetailSerializer, OrderSerializer
from drf_spectacular.utils import extend_schema

from ..pages.models import SiteSettings


class DoctorListView(APIView):
    def get(self, request, *args, **kwargs):
        doctors = Doctor.objects.all()
        serializer = DoctorListSerializer(doctors, many=True, context={'request': self.request})
        return Response(serializer.data)


class DoctorDetailView(RetrieveAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorDetailSerializer
    lookup_field = 'id'

    def get_serializer(self, *args, **kwargs):
        serializer_class = self.get_serializer_class()
        kwargs['context'] = self.get_serializer_context()
        return serializer_class(*args, **kwargs)

    def get_serializer_context(self):
        return {'request': self.request}


class OrderCreateAPIView(APIView):
    @extend_schema(request=OrderSerializer, responses=OrderSerializer)
    def post(self, request, *args, **kwargs):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            telegram_bot = SiteSettings.objects.first()
            name = serializer.validated_data['name']
            phone = serializer.validated_data['phone']
            email = serializer.validated_data['email']
            text = serializer.validated_data['text']
            docktor = serializer.validated_data['docktor'].name
            packege = serializer.validated_data['packege']
            message = f"Запись на прием\n\nИмя: {name}\nТелефон: {phone}\nEmail: {email}\nСообщение: {text}\nВрач: {docktor}\nПакет: {packege}"
            try:
                for group in telegram_bot.telegram_channels.split(","):
                    send_telegram_message(bot_token=telegram_bot.telegram_bot_id, chat_id=group, message=message)
            except Exception as e:
                print(e)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
