from django.shortcuts import render, redirect
from .models import Grade
from django.contrib import messages

def class_index(request):
    data = Grade.objects.all()
    class_data = {'data': data}
    return render(request, 'grades/grades.html', class_data)

def class_insert(request):
    grade = request.POST.get('grade')
    class_obj = Grade()
    class_obj.grade = grade
    class_obj.save()
    return redirect('grades')
    