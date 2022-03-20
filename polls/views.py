from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Goodmorning Students of Taita Taveta University.")
    

# Create your views here.
