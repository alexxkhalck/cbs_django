from django.http import HttpResponse

def home(request):
    return HttpResponse("Home page")

def Book(request, title):
    return HttpResponse(f"Book chapter: {title}")