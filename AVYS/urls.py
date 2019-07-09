"""AVYS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from bys import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.anasayfa),
    path('giris/', views.giris),
    path('AVYS/', views.AVYS),
    path('yayınekle/', views.yayınekle),
    path('projeekle/', views.projeekle),
    path('faliyetekle/', views.faliyetekle),
    path('etkinlikekle/', views.etkinlikekle),
    path('atıfekle/', views.atıfekle),
    path('patentekle/', views.patentekle),
    path('ödülekle/', views.ödülekle),
    path('Kurumun yıllara göre yayın dağılımı/', views.yayınrapor),
    path('projerapor/', views.projerapor),
    path('faliyetrapor/', views.faliyetrapor),
    path('etkinlikrapor/', views.etkinlikrapor),
    path('atıfrapor/', views.atıfrapor),
    path('patentrapor/', views.patentrapor),
    path('ödülrapor/', views.ödülrapor),
    path('cikis/', views.cikis_yap),
]