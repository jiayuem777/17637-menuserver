"""webapps URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url, include
from . import views


urlpatterns = [
    url(r'^menu/$', views.menu, name='Menu'),
    # url(r'^order/$', views.order, name='Order'),
    url(r'^dish/$', views.dish, name='Dish'),
    url(r'^menu_management/$', views.menu_management, name='Menu Management'),
    # url(r'^submitted_order/$', views.submitted_order, name='Submitted Orders'),
    ]
