from django.shortcuts import render,HttpResponse
# Create your views here.
def home(request):
    return HttpResponse("This is my home page")
def contact(request):
    return HttpResponse("This is my contact page (/contact)")    
def aboutus(request):
    return HttpResponse("This is my about us page (/about)")
def projects(request):
    return HttpResponse("This is my projects page (/projects)")        