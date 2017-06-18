"""mysite URL Configuration

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

from . import views

urlpatterns = [
	url (r'^$', views.index),

    url(r'^get_pharmacy/', views.get_pharmacy, name="get_pharmacy"),
    url(r'^create_pharmacy/', views.create_pharmacy, name="create_pharmacy"),
    url(r'^delete_pharmacy/', views.delete_pharmacy, name="delete_pharmacy"),
    url(r'^edit_pharmacy/', views.edit_pharmacy, name="edit_pharmacy"),

    url(r'^get_doctor/', views.get_doctor, name="get_doctor"),
    url(r'^create_doctor/', views.create_doctor, name="create_doctor"),
    url(r'^delete_doctor/', views.delete_doctor, name="delete_doctor"),
    url(r'^edit_doctor/', views.edit_doctor, name="edit_doctor"),

    url(r'^get_user/', views.get_user, name="get_user"),
    url(r'^create_user/', views.create_user, name="create_user"),
    url(r'^delete_user/', views.delete_user, name="delete_user"),
    url(r'^edit_user/', views.edit_user, name="edit_user"),

    url(r'^get_script/', views.get_script, name="get_script"),
    url(r'^create_script/', views.create_script, name="create_script"),
    url(r'^delete_script/', views.delete_script, name="delete_script"),
    url(r'^edit_script/', views.edit_script, name="edit_script"),

    url(r'^get_event/', views.get_event, name="get_event"),
    url(r'^create_event/', views.create_event, name="create_event"),
    url(r'^delete_event/', views.delete_event, name="delete_event"),
    url(r'^edit_event/', views.edit_event, name="edit_event"),

    url(r'^get_pharm_event/', views.get_pharm_event, name="get_pharm_event"),
    url(r'^create_pharm_event/', views.create_pharm_event, name="create_pharm_event"),
    url(r'^delete_pharm_event/', views.delete_pharm_event, name="delete_pharm_event"),
    url(r'^edit_pharm_event/', views.edit_pharm_event, name="edit_pharm_event"),

    url(r'^popdoc/', views.populate_doctors),
    url(r'^popuser/', views.populate_users),
    url(r'^poppharm/', views.populate_pharmacies),

    url(r'^admin/', admin.site.urls),
]
