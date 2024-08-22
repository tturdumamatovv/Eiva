from django.urls import path
from .views import ServiceListView, PackageListView, CategoryListView, PackageServicesListView

urlpatterns = [
    path('categories/', CategoryListView.as_view(), name='categories'),
    path('prices/<int:category_id>/', ServiceListView.as_view(), name='prices'),
    path('packages/', PackageListView.as_view(), name='packages'),
    path('packege/services/', PackageServicesListView.as_view(), name='package_services'),
]
