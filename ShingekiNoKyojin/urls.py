"""
URL configuration for ShingekiNoKyojin project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
# shingeki_project/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ShingekiNoKyojin.urls')),  
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Página inicial
    path('sobre/', views.sobre, name='sobre'),  # Página sobre o anime
    path('perfil/', views.perfil_usuario, name='perfil_usuario'),  # Página de perfil eu usei um personagem
    path('contato/', views.contato, name='contato'),  # Página de contato
]