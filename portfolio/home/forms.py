from django import forms
from home.models import *

class ContactForm(forms.ModelForm):
    class Meta:
        model = User_mod
        fields = ['number', 'message']
        widgets = {
            'number': forms.TextInput(attrs={'class': 'form-control ', 'placeholder': 'Your Phone Number', 'id': 'number', 'name': 'number'}),
            'message': forms.Textarea(attrs={'class': 'form-control textarea ', 'placeholder': 'Your Message', 'id': 'message', 'name': 'message'}),
        }
        labels = {
            'number': 'Contact Number',
            'message': 'Any message for me?',
        }
class User1(forms.ModelForm):#used in login form
    class Meta:

        model = user
        fields = ['name', 'email', 'password']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': ' UserName', 'id': 'name', 'name': 'name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email', 'id': 'mail', 'name': 'mail'}),
            'password': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Password', 'id': 'password', 'name': 'password'}),
            }
        labels = {
            'name': 'Name',
            'email': 'Email',
            'password': 'Password',
        }
class User_Form(forms.ModelForm):#used in signin
    class Meta:
        model = User_mod
        fields = ['name', 'email', 'password']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'UserName', 'id': 'name', 'name': 'name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': '  Your Email', 'id': 'mail', 'name': 'mail'}),
            'password': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your password', 'id': 'password', 'name': 'password'}),
            }
        labels = {
            'name': 'Name',
            'email': 'Email',
            'password': 'Password',
        }        
