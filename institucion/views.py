from django.shortcuts import render,HttpResponse

# Create your views here.

def index(request):
    return render(request,"institucion/index.html")

def other_page(request):
    return render(request,"institucion/otherPage.html")