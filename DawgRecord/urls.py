"""DawgRecord URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.contrib.auth import login, logout
from registro import views
from django.conf.urls import url, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from api.api import UserAPI 
from django.views.generic import TemplateView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
  #  url(r'^login/', views.Login, name= 'login'),
    url(r'^$', views.inicio, name= 'index'),
   # url(r'^logout/', views.logout_request, name= 'logout'),
   # url(r'^login/', views.login_request, name= 'login'),
    url(r'^servicios/', views.servicios, name= 'servicios'),
    url(r'^artistas/', views.artistas, name= 'artistas'),
    url(r'^dref/', views.dref, name= 'dref'),
    url(r'^chriz/', views.Chriz, name= 'chriz'),
    url(r'^post/', views.PoztMalone, name= 'post'),
    url(r'^api/1.0/create_user/', UserAPI.as_view(), name = "api_create_user"),
    url(r'^accounts/', include('allauth.urls')),
    url('', TemplateView.as_view(template_name="login/index.html")),
    url(r'^zerv/', views.zervicioz, name= 'zervicioz'),
    url(r'^princi/', views.princi, name= 'princi'),

    
]

urlpatterns += staticfiles_urlpatterns()