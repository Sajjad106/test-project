from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages 

def batch(request):
    return HttpResponse("This is batch")