from rest_framework.generics import RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Doctor
from .serializers import DoctorListSerializer, DoctorDetailSerializer


class DoctorListView(APIView):
    def get(self, request, *args, **kwargs):
        doctors = Doctor.objects.all()
        serializer = DoctorListSerializer(doctors, many=True)
        return Response(serializer.data)


class DoctorDetailView(RetrieveAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorDetailSerializer
    lookup_field = 'id'
