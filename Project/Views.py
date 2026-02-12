from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'site/home.html')

def sobre(request):
    return render(request, 'site/sobre.html')

