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
from django.conf import settings
from django.conf.urls.static import static
from menuserver import views
# from django.views.static import serve　


urlpatterns = [
    url(r'^$', views.main, name='Main'),
    url(r'^main/', views.main, name='Main'),
    url(r'^menu/', views.menu, name='Menu'),
    url(r'^order/', views.order, name='Order'),
    url(r'^dish/', views.dish, name='Dish'),
    url(r'^store/', views.store, name='Store'),
    url(r'^manager/', views.manager, name='Manager'),
    url(r'^employee/', views.employee, name='Employee'),
    url(r'^menu_management/', views.menu_management, name='Menu Management'),
    url(r'^submitted_order/', views.submitted_order, name='Submitted Orders'),
    url(r'^store_manager_employee/', views.store_manager_employee, name='Management'),
    url(r'^register/', views.register, name='Register'),
    url(r'^login/', views.user_login, name='Login'),
    url(r'^logout/', views.user_logout, name='Logout'),
    url(r'^error/', views.error, name='Error'),
    url(r'^admin/', admin.site.urls),
    url(r'^ajax_increase/', views.ajax_increase, name='ajax_increase'),
    url(r'^ajax_decrease/', views.ajax_decrease, name='ajax_decrease'),
    url(r'^ajax_reload/', views.ajax_reload, name='ajax_reload'),
    url(r'^ajax_addOrder/', views.ajax_addOrder, name='ajax_addOrder'),
    # url(r'^media/(?P<path>.*)$', serve, {'document_root':settings.MEDIA_ROOT}),　　#这部分很重要

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
