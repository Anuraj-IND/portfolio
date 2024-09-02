from django.shortcuts import render,HttpResponse
# Create your views here.
def home(request):
    d={'name':"Anuraj",'course':"Django",'language':"python"}
    return render(request,'home.html',d)
def contact(request):
    return render(request,'contact.html')
def about(request):
    return render(request,'about.html')
def project(request):
    return render(request,'project.html')        