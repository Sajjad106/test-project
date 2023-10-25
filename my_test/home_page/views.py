from django.shortcuts import render, HttpResponse

def home_index(request):
    return render(request, 'user/home.html')


