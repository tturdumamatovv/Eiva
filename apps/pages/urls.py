from django.urls import path
from . import views

urlpatterns = [
    path('welcome/', views.WelcomePageView.as_view(), name='index'),
    # path('home/', views.contact, name='contact'),
    # path('about/', views.about, name='about'),
    # path('services/', views.services, name='services'),
    # path('contacts/', views.contact, name='contact'),
    # path('docktors/', views.gallery, name='gallery'),
]

