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
    
    data= (student_name,grade,mothers_name,fathers_name,guardians_name,date_of_birth,contact_no,present_address,permanent_address)
    student_data = {'data': data}
    
    if student_data: 
        if len(student_name)==0:
            messages.success(request, "Student Name is required")
        elif len(grade)==0:
            messages.success(request, "CLass is required")
        elif len(mothers_name)==0:
            messages.success(request, "Mother's Name is required")
        elif len(fathers_name)==0:
            messages.success(request, "Father's Name is required")
        elif len(guardians_name)==0:
            messages.success(request, "Guardian's Name is required")
        elif len(date_of_birth)==0:
            messages.success(request, "Date of Birth is required")
        elif len(contact_no)==0:
            messages.success(request, "Contact No. is required")
        elif len(present_address)==0:
            messages.success(request, "Present Address is required")
        elif len(permanent_address)==0:
            messages.success(request, "Permanent Address is required")
        
                
                
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
    else:
        messages.success(request, 'The fields can not be empty')
    
    return redirect('studentadmin')

    
    
#Student information edit
def edit_index(request,id):
    st_obj = StudentEntry.objects.get(id=id)
    single_student = {'Student_data': st_obj, 'id': id}
    return render(request, 'admin/student_edit.html', single_student)

#Student information delete
def delete_index(request,id):
    st_obj = StudentEntry.objects.get(id=id)
    st_obj.delete() #delete from table where id = id
    return redirect('studentadmin')

def update(request):
    student_name = request.POST.get('student_name')
    student_id = request.POST.get('student_id')
    grade = request.POST.get('grade')
    mothers_name = request.POST.get('mothers_name')
    fathers_name = request.POST.get('fathers_name')
    guardians_name = request.POST.get('guardians_name')
    date_of_birth = request.POST.get('date_of_birth')
    contact_no = request.POST.get('contact_no')
    present_address = request.POST.get('present_address')
    permanent_address = request.POST.get('permanent_address')
    
    data= (student_name,grade,mothers_name,fathers_name,guardians_name,date_of_birth,contact_no,present_address,permanent_address)
    student_data = {'data': data}
    
    if student_data: 
        if len(student_name)==0:
            messages.success(request, "Student Name is required")
        elif len(grade)==0:
            messages.success(request, "Class is required")
        elif len(mothers_name)==0:
            messages.success(request, "Mother's Name is required")
        elif len(fathers_name)==0:
            messages.success(request, "Father's Name is required")
        elif len(guardians_name)==0:
            messages.success(request, "Guardian's Name is required")
        elif len(date_of_birth)==0:
            messages.success(request, "Date of Birth is required")
        elif len(contact_no)==0:
            messages.success(request, "Contact No. is required")
        elif len(present_address)==0:
            messages.success(request, "Present Address is required")
        elif len(permanent_address)==0:
            messages.success(request, "Permanent Address is required")
        
                
                
        else:
            st_obj = StudentEntry.objects.get(id=student_id)
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
            messages.success(request, "Student Information Updated Successfully")
    else:
        messages.success(request, 'The fields can not be empty')
    
    return redirect('studentadmin')
