from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.
def view_home(request: HttpRequest) -> HttpResponse:
    return render(request, 'core/home.page.html', context={"value" : "George"})  # Utilise le template

def view_dynamic(request: HttpRequest, number: int = 0):
    return HttpResponse(f"J'ai reçu {number}") #fonction pour URL dynamique

def hello_core(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Hello World depuis Core !") #fonction pour sous-URL