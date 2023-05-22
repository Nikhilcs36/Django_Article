from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>hi its me nikhil cool</h1>')

def about(request):
    return HttpResponse("about us page  ")
