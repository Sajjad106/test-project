from django.shortcuts import render, HttpResponse, redirect
from .models import StudentEntry 
from django.contrib import messages 

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
    

    if not student_name or not grade or not mothers_name or not fathers_name or not guardians_name or not date_of_birth or not contact_no or not present_address or not permanent_address:
        messages.success(request, "All fields are required")
    else:
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
        messages.success(request, "Student Information Inserted Successfully")
    
    return redirect('studentadmin')

    
    
    
def edit_index(request,id):
    cat_id = {'id' :id}
    return render(request, 'admin/student_edit.html', cat_id)

