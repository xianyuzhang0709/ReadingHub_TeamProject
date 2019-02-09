from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    response = render(request, 'readinghub/index.html')
    return response

def about(request):
    response = render(request, 'readinghub/about.html')
    return response

def register(request):
    response = render(request, 'readinghub/register.html')
    return response

def login(request):
    response = render(request, 'readinghub/login.html')
    return response

def logout(request):
    return 0

def event(request):
    response = render(request, 'readinghub/event.html')
    return response

def book(request):
    response = render(request, 'readinghub/book.html')
    return response






