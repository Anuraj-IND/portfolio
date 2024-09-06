from django.shortcuts import render,HttpResponse
from home.models import Contact
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
def contactadd(request):
    try:
        if request.method == 'POST':
            name=request.POST['name']
            mail=request.POST['mail']
            number=request.POST['number']
            message=request.POST['message']
            print(name,mail,number,message)
            Contact.objects.create(name=name,email=mail,number=number,message=message)
            return HttpResponse("Contact added successfully")
            print("added")
            return render(request,'contact.html')    
    except Exception as e:
        return HttpResponse(e)