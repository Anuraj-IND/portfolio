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
                        ufrm=User1()
                        return render(request,'signin.html',{"ufrm":ufrm})     
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
              
def message(request):
    if request.session.has_key('username') and request.session['password']:
        try:
            message=User_mod.objects.filter(message__isnull=False)
            
            return render(request,'messages.html',{'messages':message})
        except Exception as e:
            return HttpResponse(e)
    else:
          return redirect('displaylogin')  

def deleted(request): 
            try:
                del_name=request.GET['del_name']
                if request.session['username'] == del_name:
                    dell=User_mod.objects.get(name=del_name)
                    dell.message=None
                    dell.save()#i want to delete message only not whole row of user how to do it?
                    return message(request)
                else :
                    return message(request)    
            except Exception as e:
                print(e)
                return HttpResponse(e)
                                     
def about(request):
    if request.session.has_key('username') and request.session['password']:
      return render(request,'about.html')
    else:
          return redirect('displaylogin')  
def project(request):
  if request.session.has_key('username') and request.session['password']:  
    return render(request,'project.html') 
  else:
          return redirect('displaylogin')         