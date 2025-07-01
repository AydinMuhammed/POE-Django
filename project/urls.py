"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from core.views import view_home
from core.views import view_dynamic

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", view_home, name="home"), #chemin url simple, page d'accueil comme ya pas de précision
    path("dyn/<int:number>", view_dynamic, name='dynamic'), #chemin URL dynamique : dyn/nombre
    #pour tester seulement 0 ou entier positif http://127.0.0.1:8000/dyn/50
    path("core/", include("core.urls")), #chemin pour la sous-URL : core/
    #pour tester http://127.0.0.1:8000/core/
]