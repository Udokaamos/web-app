from django.http import response
from django.test import TestCase
from django.urls import reverse, resolve
from .views import school_page, services_page, features_page 
# Create your tests here.

class ViewTestCase(TestCase):

    def test_school_view(self):
        res = resolve(reverse("school"))
        response = self.client.get(reverse("school"))
        self.assertEqual(200, response.status_code)
        self.assertEqual(response.content, b"This is a good site")
        self.assertEqual(res.func, school_page)

    def test_services_view(self):
        res = resolve(reverse("services"))
        response = self.client.get(reverse("services"))
        self.assertEqual(200, response.status_code)
        self.assertEqual(response.content, b"This is backend with python on Django framework")
        self.assertEqual(res.func, services_page )
    
    def test_features_view(self):
        res = resolve(reverse("feature"))
        response = self.client.get(reverse("feature"))
        self.assertEqual(200, response.status_code)
        self.assertEqual(response.content, b"This is our services")
        self.assertEqual(res.func, features_page)