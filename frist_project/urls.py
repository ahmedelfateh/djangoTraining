"""frist_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from frist_app import views
from django.conf.urls import include

urlpatterns = [
    url(r'^new/', include("frist_app.urls")),
    url(r'^$', views.index, name="index"),
    url(r'^help/', views.help, name="help"),
    # url(r'^mod/', views.modtest, name="modtest"),
    url(r'^userdata/', views.userFunc, name="userdata"),
    url(r'^mod/', views.modnew, name="model"),
    url(r'^form', views.formName, name="form"),
    #url for the landing page
    url(r'^lp/', views.newUser, name="lp"),
    url(r'^admin/', admin.site.urls),
]
