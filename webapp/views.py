from django.shortcuts import render
from . models import Destination
# Create your views here.
def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def news(request):
    return render(request,'news.html')

def register(request):
    return render(request,'register.html')


def index(request):
    dests=Destination.objects.all
    return render(request,"index.html",{'dests':dests})