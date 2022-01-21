from django.shortcuts import render
from django.http.response import HttpResponse
# Create your views here.

def school_page(request):
    return HttpResponse("This is a good site")

def services_page(request):
    return HttpResponse("This is backend with python on Django framework")

def features_page(request):
    return HttpResponse("This is our services")