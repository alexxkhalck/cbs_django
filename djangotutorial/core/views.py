from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html', {
        "title": "Home Page",
        "text": "This is the home page of the core app."
    }) #core/

def about(request):
    return render(request, 'about.html', {
        "title": "About Page",
        "text": "This is the about page of the core app."
    }) #core/