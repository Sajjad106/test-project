from django.shortcuts import render, HttpResponse

def student(request):
    return render(request, 'admin/student.html') 
def insert(request):
    student_name = request.POST.get('student_name')
    class_ = request.POST.get('class_')
    mothers_name = request.POST.get('mothers_name')
    fathers_name = request.POST.get('fathers_name')
    gurdian_name = request.POST.get('gurdian_name')
    date_of_birth = request.POST.get('date_of_birth')
    contact_no = request.POST.get('contact_no')
    persent_adress = request.POST.get('persent_adress')
    permanent_adress = request.POST.get('permanent_adress')
    data = [student_name, class_, mothers_name, fathers_name, gurdian_name, date_of_birth, contact_no, persent_adress, permanent_adress]
    return HttpResponse(data)

# def insert(request):
#     class_ = request.POST.get('class_')
#     return HttpResponse(class_)
# def insert(request):
#     mothers_name = request.POST.get('mothers_name')
#     return HttpResponse(mothers_name)
# def insert(request):
#     fathers_name = request.POST.get('fathers_name')
#     return HttpResponse(fathers_name)
# def insert(request):
#     gurdian_name = request.POST.get('gurdian_name')
#     return HttpResponse(gurdian_name)
# def insert(request):
#     date_of_birth = request.POST.get('date_of_birth')
#     return HttpResponse(date_of_birth)
# def insert(request):
#     contact_no = request.POST.get('contact_no')
#     return HttpResponse(contact_no)
# def insert(request):
#     persent_adress = request.POST.get('persent_adress')
#     return HttpResponse(persent_adress)
# def insert(request):
#     permanent_adress = request.POST.get('permanent_adress')
#     return HttpResponse(permanent_adress)


  

