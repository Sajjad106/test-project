from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages 

def batch(request):
    return render(request, 'admin/batch.html')