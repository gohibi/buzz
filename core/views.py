from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')

def customer_page(request):
    pass

def courier_page(request):
    pass