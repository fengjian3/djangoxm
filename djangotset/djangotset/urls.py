"""djangotset URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from polls import views
from django.conf.urls import url

# 页面编辑（添加页面

urlpatterns = [
    path('index/', views.index, name='index'),

    path('login/', views.login, name='login'),

    path('empty/', views.empty, name='empty'),

    path('form/', views.form, name='form'),

    path('morris/', views.morris, name='morris'),

    path('tabpanel/', views.tabpanel, name='tabpanel'),

    path('table/', views.table, name='table'),

    path('tpl/', views.tpl, name='tpl'),

    path('', views.login)

]


