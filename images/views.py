from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def get(request):
    return HttpResponse("It works")