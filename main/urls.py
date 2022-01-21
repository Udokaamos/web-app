from django.urls import path
from .views import home_page, about_page, contact_us, services_page

urlpatterns = [
    path('home/', home_page, name="home"),
    path('about/', about_page, name="about"),
    path('contact/', contact_us, name= "contact"),
    path('service/', services_page, name="service"),
]
