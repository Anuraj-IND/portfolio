from django import forms
from home.models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'number', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name', 'id': 'name', 'name': 'name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email', 'id': 'mail', 'name': 'mail'}),
            'number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Phone Number', 'id': 'number', 'name': 'number'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Your Message', 'id': 'message', 'name': 'message'}),
        }
