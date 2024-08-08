from django.urls import path
from . import views

urlpatterns = [
    path('welcome/', views.WelcomePageAPIView.as_view(), name='welcome'),
    path('main/', views.MainPageAPIView.as_view(), name='main'),
    path('contacts/', views.ContactInformationView.as_view(), name='contact-information'),

    path('about/', views.AboutPageAPIView.as_view(), name='about'),
    # path('services/', views.services, name='services'),
    # path('contacts/', views.contact, name='contact'),
    # path('docktors/', views.gallery, name='gallery'),
]

