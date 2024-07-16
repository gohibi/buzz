from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from core.forms import SignupForm
from django.contrib.auth import login,authenticate
from . import forms
# Create your views here.
def home(request):
    return render(request,'home.html')

@login_required()
def customer_page(request):
    return render(request,'home.html')


@login_required()
def courier_page(request):
    return render(request,'home.html')

def signup(request):
    if request.method == "POST":
        form =forms.SignupForm(request.POST)
        
        if form.is_valid():
            email =form.cleaned_data.get('email').lower()
            user = form.save(commit=False)
            user.username = email
            user.save()
            
            login(request,user)
            return redirect('/')
    else:
        form = SignupForm()
    
    context={
        'form':form
    }
    return render(request,'signup.html',context)