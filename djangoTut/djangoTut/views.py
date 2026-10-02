from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hello World, You are at Home")
    return render(request, 'index.html')


def about(request):
    # return HttpResponse("Hello World, You are at about")
    return render(request, 'about.html')


def contact(request):
    # return HttpResponse("Hello World, You are at contact")
    return render(request, 'contact.html')