from django.http import response
from django.test import TestCase
from django.urls import reverse, resolve
from .views import home_page, about_page, contact_us, services_page
# Create your tests here.

class ViewTestCase(TestCase):

    def test_home_view(self):
        res = resolve(reverse("home"))
        response = self.client.get(reverse("home"))
        self.assertEqual(200, response.status_code)
        self.assertContains(response, "Home Page")
        # self.assertEqual(response.content, b"This is a good site")
        self.assertEqual(res.func, home_page)
        self.assertTemplateUsed(response, 'home.html')
        self.assertTemplateUsed(response, "base.html")
        self.assertContains(response, 'ecommerce.css')

    def test_page_view(self):
        res = resolve(reverse("about"))
        response = self.client.get(reverse("about"))
        self.assertEqual(200, response.status_code)
        self.assertContains(response, "About Us")
        # self.assertEqual(response.content, b"This is backend with python on Django framework")
        self.assertEqual(res.func, about_page )
        self.assertTemplateUsed(response,'about.html')
        self.assertTemplateUsed(response, "base.html")
        self.assertContains(response, 'ecommerce.css')

    def test_contact_view(self):
        res = resolve(reverse("contact"))
        response = self.client.get(reverse("contact"))
        self.assertEquals(200, response.status_code)
        # self.assertEqual(response.content, b"<p>Lorem ipsum dolor sit amet consectetur, adipisicing elit. Illum velit nostrum, earum in deleniti nam quo rerum architecto ad, quasi corrupti. Nostrum quod nihil temporibus dolore iure nemo optio reprehenderit?</p>")
        self.assertContains(response, "Contact Us")
        self.assertEquals(res.func, contact_us)
        self.assertTemplateUsed(response, 'contact.html')
        self.assertTemplateUsed(response, "base.html")
        self.assertContains(response, 'ecommerce.css')


    
    def test_service_view(self):
        res = resolve(reverse("service"))
        response = self.client.get(reverse("service"))
        self.assertEqual(200, response.status_code)
        self.assertContains(response, "Our Services")
        # self.assertEqual(response.content, b"This is our services")
        self.assertEqual(res.func, services_page)
        self.assertTemplateUsed(response, "services.html")
        self.assertTemplateUsed(response, "base.html")
        self.assertContains(response, 'ecommerce.css')