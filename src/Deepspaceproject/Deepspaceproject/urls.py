"""Deepspaceproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url

from product.views import fetch_view
from product.views import created_view2
from product.views import new_view

urlpatterns = [
    # path('admin/', admin.site.urls),
    url(r'^admin/', admin.site.urls),
    url('created2/(?P<slug>[\w-]+)/$', created_view2,name='created2'),
    path('', new_view,name='new_view'),
    url('^(?P<slug>[\w-]+)/$',fetch_view,name='fetchview'),
    #path('',    home_view,name='home2'),
]
