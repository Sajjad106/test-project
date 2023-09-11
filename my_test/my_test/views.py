from django.shortcuts import render, HttpResponse, redirect
from .models import StudentEntry 
from django.contrib import messages as messages

def student(request):
    return render(request, 'admin/student.html') 
def insert(request):
    student_name = request.POST.get('student_name')
    grade = request.POST.get('grade')
    mothers_name = request.POST.get('mothers_name')
    fathers_name = request.POST.get('fathers_name')
    gurdian_name = request.POST.get('gurdian_name')
    date_of_birth = request.POST.get('date_of_birth')
    contact_no = request.POST.get('contact_no')
    persent_adress = request.POST.get('persent_adress')
    permanent_adress = request.POST.get('permanent_adress')
    
    st_obj = StudentEntry()
    st_obj.name = student_name
    st_obj.grade = grade
    st_obj.mothers_name = mothers_name
    st_obj.fathers_name = fathers_name
    st_obj.gurdians_name = gurdian_name
    st_obj.date_of_birth = date_of_birth
    st_obj.contact_no = contact_no
    st_obj.peresent_adress = persent_adress
    st_obj.permanent_adress = permanent_adress
    st_obj.save()
    messages.success(request, "Student Information Inserted Successfully")
    return redirect('studentadmin')

  

