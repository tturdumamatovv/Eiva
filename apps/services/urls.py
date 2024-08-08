from django.urls import path
from . import views

urlpatterns = [
    path('services/', views.CategoryListAPIView.as_view(), name='services'),

]
