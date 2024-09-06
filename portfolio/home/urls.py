from django.contrib import admin
from django.urls import path,include
from home import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact', views.contact, name='contact'),
    path('project', views.project, name='project'),
    path('about', views.about, name='about'),
    path('contact_saved', views.contactadd, name='contact_add')
]