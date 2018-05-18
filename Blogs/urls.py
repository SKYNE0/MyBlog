# -*- coding: UTF-8 -*- 
"""MyBlogs URL Configuration

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

from . import views

app_name = "Blogs"

urlpatterns = [
        url(r'^$', views.Index.as_view(), name='index'),
        url (r'^detail/$', views.detail, name='detail'),
        url(r'^archives/$', views.Archives.as_view(), name='archives'),
        url(r'^archive/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.archive, name='archives_list'),
        url(r'^label/(?P<tag_id>[0-9]+)/$', views.Label.as_view(), name='label'),
        url(r'^category/(?P<category_id>[0-9]+)/$', views.Categorys.as_view(), name='category'),

]
