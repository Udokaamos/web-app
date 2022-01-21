from django.urls import path
from .views import school_page, services_page, features_page

urlpatterns = [
    path('school/', school_page, name="school"),
    path('services/', services_page, name="services"),
    path('features/', features_page, name="feature"),
]