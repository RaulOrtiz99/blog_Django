from django.shortcuts import render

# Create your views here.

def home(request):
    nombre= 'Admin'
    return render(request,'app/home.html',{'nombre':nombre})