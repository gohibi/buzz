from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class SignupForm(UserCreationForm):
    email =forms.EmailField(max_length=200)
    first_name =forms.CharField(max_length=150)
    last_name = forms.CharField(max_length=150)
    
    class Meta:
        model = User
        fields = ['email','first_name','last_name','password1','password2']
        
    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        if User.objects.filter(email=email):
            raise ValidationError('cet email existe deja')
        return email