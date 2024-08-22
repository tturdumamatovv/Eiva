from rest_framework.generics import RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Doctor
from .serializers import DoctorListSerializer, DoctorDetailSerializer


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
