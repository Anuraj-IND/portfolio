from django.contrib import admin
from django.urls import path,include
from home import views

urlpatterns = [
    path('', views.sign, name='sign'),
    path('signin', views.signin, name='signin'),
    path('login', views.login, name='login'),
    path('displaylogin', views.displaylogin, name='displaylogin'),
    path('home', views.home, name='home'),
    path('contact', views.displaycontactform, name='contact'),
    path('add_contact', views.add_contact, name='add_contact'),
    path('message', views.message, name='message'),
    path('delete', views.deleted, name='delete'),
    # path('project', views.project, name='project'),
    # path('about', views.about, name='about'),
]