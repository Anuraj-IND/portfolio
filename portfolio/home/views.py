from django.shortcuts import render,HttpResponse,redirect
from home.models import Contact
from home.forms import ContactForm
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
def add_contact(request):
                    if request.method == 'POST':
                        cfrm=ContactForm(request.POST)
                    try:
                        if cfrm.is_valid():
                                cfrm.save()
                                print("saved",cfrm)
                        return redirect('contact')
                    except Exception as e:
                        return HttpResponse(str(e))     
                    else:
                        return render(request,'contact.html',{'form':cfrm})            
def displaycontactform(request):
     cfrm=ContactForm()
     return render(request,'contact.html',{"cfrm":cfrm})    
                                     
              
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