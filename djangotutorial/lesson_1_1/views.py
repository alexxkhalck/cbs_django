from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Lesson 1_1 has created and works!")