from django.shortcuts import render,HttpResponse,redirect
from home.models import *
from home.forms import ContactForm,User1,User_Form
# Create your views here.
def sign(request):
    ufrm=User1()
    return render(request,'signin.html',{"ufrm":ufrm})  
def signin(request):
         if request.method == 'POST':
                    ufrm=User_Form(request.POST)
                    try:
                        if ufrm.is_valid():
                                ufrm.save()
                                print("saved",ufrm)
                        return redirect('displaylogin')
                    except Exception as e:
                        return HttpResponse(str(e))     
                    else:
                        return render(request,'signin.html')      
def login(request):
    if request.method == 'POST':
        name=request.POST['name']
        password=request.POST['password']
        try:
            
            if User_mod.objects.filter(name=name,password=password):
                request.session['username']=name
                request.session['password']=password
                return render(request, 'home.html', {'username':name, 'password':password})
            else:
                ufrm=User_Form()
                return render(request, 'login.html',{"ufrm":ufrm})
        except Exception as e:
            ufrm=User_Form()
            return render(request, 'login.html',{"ufrm":ufrm}) 
    else:
        ufrm=User_Form()
        return render(request, 'login.html',{"ufrm":ufrm})
def displaylogin(request):
    ufrm=User_Form()
    return render(request,'login.html',{"ufrm":ufrm})  

def home(request):
    if request.session.has_key('username') and request.session['password']:
                 return render(request,'home.html')
    else:
        return redirect('displaylogin')             
def displaycontactform(request):
  if request.session.has_key('username') and request.session['password']:
     print(request.session['username'],request.session['password'])
     cfrm=ContactForm()
     return render(request,'contact.html',{"cfrm":cfrm}) 
  else:
        return redirect('displaylogin')     
def add_contact(request):
    if(1==1):
        username=request.session['username']
        # password=request.session['password']
        try:
                user = User_mod.objects.get(name=username)  # ye ban gaya objevt jiska name username se matvh karega
                if request.method == 'POST':
                    cfrm=ContactForm(request.POST)
                    try:
                      if cfrm.is_valid():
                        user.message = cfrm.cleaned_data.get('message')
                        user.number = cfrm.cleaned_data.get('number')
                        user.save()
                        print("saved",user)
                        return redirect('contact')
                      else:
                        return render(request,'contact.html',{'form':cfrm})    
                    except Exception as e:
                       return HttpResponse(str(e))     
        except Exception as e:
                return HttpResponse("User not found in the database")    
    else:
         return redirect('displaylogin')                                      
# def contact(request):
#      return render(request,'contact.html')
# def about(request):
#     return render(request,'about.html')
# def project(request):
#     return render(request,'project.html')        
              
# def message(request):
#     try:
#         message=Contact.objects.all()
#         return render(request,'messages.html',{'messages':message})
#     except Exception as e:
#         return HttpResponse(e)
# def deleted(request):
#     try:
#         del_id=request.GET['del_id']
#         dell=Contact.objects.get(id=del_id)
#         dell.delete()
#         return message(request)
#     except Exception as e:
#         print(e)
#         return HttpResponse(e)
                                     