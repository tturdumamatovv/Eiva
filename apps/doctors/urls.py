from django.urls import path
from .views import DoctorListView, DoctorDetailView, OrderCreateAPIView

urlpatterns = [
    path('doctors/', DoctorListView.as_view(), name='doctor-list'),
    path('doctors/<int:id>/', DoctorDetailView.as_view(), name='doctor-detail'),
    path('order/', OrderCreateAPIView.as_view(), name='create_order'),

]
