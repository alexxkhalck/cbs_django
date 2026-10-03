from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'lesson_1_1/index.html')