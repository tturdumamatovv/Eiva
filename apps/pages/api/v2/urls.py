from django.urls import path
from . import views
from ..v1.views import WelcomePageAPIView

urlpatterns = [
    # MAIN PAGE

    path('main/our-services/', views.MainPageOurServicesAPIView.as_view(), name='main-our-services'),
    path('main/our-specialists/', views.MainPageOurSpecialistsAPIView.as_view(), name='main-our-specialists'),
    path('main/about-us/', views.MainPageAboutUsAPIView.as_view(), name='main-about-us'),
    path('main/birth-counter/', views.MainPageBirthCounterAPIView.as_view(), name='main-birth-counter'),

    # ABOuT PAGE

    path('about/abuout-us/', views.AboutPageAboutUsAPIView.as_view(), name='about-about-us'),
    path('about/include/', views.AboutPageIncludeAPIView.as_view(), name='about-include'),
    path('about/faq/', views.AboutPageFAQAPIView.as_view(), name='about-faq'),
    path('about/parents/', views.AboutPageParentsAPIView.as_view(), name='about-parents'),
    path('about/gallery/', views.AboutPageGalleryAPIView.as_view(), name='about-gallery'),


]
