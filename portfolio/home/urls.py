from django.contrib import admin
from django.urls import path,include
from home import views

urlpatterns = [
    path('', views.sign, name='sign'),
    path('home', views.home, name='home'),
    path('add_contact', views.add_contact, name='add_contact'),
    path('project', views.project, name='project'),
    path('about', views.about, name='about'),
    path('message', views.message, name='message'),
    path('delete', views.deleted, name='delete'),
    path('contact', views.displaycontactform, name='contact'),
    path('login', views.signin, name='login'),
]