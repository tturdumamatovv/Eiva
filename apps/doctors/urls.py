from django.urls import path
from .views import DoctorListView, DoctorDetailView

urlpatterns = [
    path('doctors/', DoctorListView.as_view(), name='doctor-list'),
    path('doctors/<int:id>/', DoctorDetailView.as_view(), name='doctor-detail'),
]
