from django.urls import path
from core.views import hello_core

urlpatterns = [
    path("", hello_core, name="hello_core"), #chemin url simple, page d'accueil comme ya pas de précision
]