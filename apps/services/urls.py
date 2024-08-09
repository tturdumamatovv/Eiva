from django.urls import path
from . import views

urlpatterns = [
    path('services/', views.CategoryListAPIView.as_view(), name='services'),
    path('services/<int:pk>/', views.CategoryAPIView.as_view(), name='service'),

]
