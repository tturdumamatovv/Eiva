from rest_framework import serializers
from .models import Doctor, Position, Specialization, Сertificate, Review, Photo


class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Сertificate
        fields = ('name', 'file')


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('patient_name', 'text')


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ('file',)


class DoctorListSerializer(serializers.ModelSerializer):
    position = serializers.SerializerMethodField()
    specialization = serializers.SerializerMethodField()

    def get_position(self, obj):
        return obj.position.name
    def get_specialization(self, obj):
        return obj.specialization.name

    class Meta:
        model = Doctor
        fields = ('id', 'name', 'position', 'specialization', 'seniority', 'photo', )


class DoctorDetailSerializer(serializers.ModelSerializer):
    position = serializers.StringRelatedField()
    specialization = serializers.StringRelatedField()
    certificates = CertificateSerializer(many=True, read_only=True)
    reviews = ReviewSerializer(many=True, read_only=True)
    photos = PhotoSerializer(many=True, read_only=True)

    class Meta:
        model = Doctor
        fields = ('name', 'position', 'specialization', 'seniority', 'description', 'certificates', 'reviews', 'photos')
