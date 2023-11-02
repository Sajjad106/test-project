from django.shortcuts import render, redirect
from .models import Grade
from django.contrib import messages

def class_index(request):
    grade_data = Grade.objects.all().order_by('-id')
    data = {'data': grade_data}
    return render(request, 'grades/grades.html', data)

def class_insert(request):
    grade = request.POST.get('grade')
    class_obj = Grade()
    class_obj.grade = grade
    class_obj.save()
    return redirect('grades')
