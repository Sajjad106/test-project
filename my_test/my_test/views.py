from django.shortcuts import render, HttpResponse

def student(request):
    return render(request, 'admin/basic_elements.html') 