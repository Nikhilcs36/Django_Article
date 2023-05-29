from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"
        # fields = ("name","email","message")
        # exclude =('name',)
        
        widgets = {
            "name": forms.TextInput(attrs={'class':'form-control', 'placeholder':'enter name'}),
            "email": forms.EmailInput(attrs={'class':'form-control', 'placeholder':'enter email'}),
            "phone_number": forms.NumberInput(attrs={'class':'form-control', 'placeholder':'enter phone number'}),
            "message": forms.Textarea(attrs={'class':'form-control', 'placeholder':'enter message'}),
        }
        
        