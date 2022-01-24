import email
from email import message
from django.shortcuts import render
from django.http.response import HttpResponse

from .models import Contact

# with open('user.txt','r') as file:
#     doc = file.read()
#     user = eval(doc)

# Create your views here.
def home_page(request):
    return render(request, "home.html")

def about_page(request):
    return render(request, "about.html")

def contact_us(request):
    if request.method=="POST":
        request_data = dict(request.POST)
        request_data.pop('csrfmiddlewaretoken')
        data = {key:request_data.get(key)[0] for key in request_data}
        Contact.objects.create(name=data["my_name"], email=data["my_email"], message=data["my_message"])
        # print(data)
    # with open('user.txt', 'w') as file:
    #     file.write(f'{user}')    
    #   print(request.POST)
    return render(request, "contact.html")

def services_page(request):
    return render(request, "services.html")    