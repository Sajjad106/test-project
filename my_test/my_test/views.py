from django.shortcuts import render, HttpResponse, redirect
from .models import StudentEntry 
from django.contrib import messages as messages

def student(request):
    studententry = StudentEntry.objects.all()
    student_data = {"data":studententry}
    return render(request, 'admin/student.html', student_data) 
def insert(request):
    student_name = request.POST.get('student_name')
    grade = request.POST.get('grade')
    mothers_name = request.POST.get('mothers_name')
    fathers_name = request.POST.get('fathers_name')
    guardians_name = request.POST.get('guardians_name')
    date_of_birth = request.POST.get('date_of_birth')
    contact_no = request.POST.get('contact_no')
    present_address = request.POST.get('present_address')
    permanent_address = request.POST.get('permanent_address')
    
    st_obj = StudentEntry()
    
    st_obj.name = student_name
    st_obj.grade = grade
    st_obj.mothers_name = mothers_name
    st_obj.fathers_name = fathers_name
    st_obj.guardians_name = guardians_name
    st_obj.date_of_birth = date_of_birth
    st_obj.contact_no = contact_no
    st_obj.present_address = present_address
    st_obj.permanent_address = permanent_address
    st_obj.save()
    st = [student_name, st_obj, st_obj.mothers_name, st_obj.fathers_name, st_obj.guardians_name, st_obj.date_of_birth, st_obj.contact_no, st_obj.present_address, st_obj.permanent_address]
    
    
    messages.success(request, "Student Information Inserted Successfully")
    
    return redirect('studentadmin')

def edit_index(request,id):
    return HttpResponse (id)

