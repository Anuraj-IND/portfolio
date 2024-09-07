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
            print("added")
            return render(request,'contact.html')    
    except Exception as e:
        return HttpResponse(e)
def message(request):
    try:
        message=Contact.objects.all()
        return render(request,'messages.html',{'messages':message})
    except Exception as e:
        return HttpResponse(e)
def deleted(request):
    try:
        del_id=request.GET['del_id']
        dell=Contact.objects.get(id=del_id)
        dell.delete()
        return message(request)
    except Exception as e:
        print(e)
        return HttpResponse(e)