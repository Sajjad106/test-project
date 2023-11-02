from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages 
from .models import Batch
from grades.models import Grade

def batch(request):
    grade_data = Grade.objects.all().order_by('-id')
    all_batch = Batch.objects.all().order_by('-batch_id')
    data = {'grades_data': grade_data, 'batch_data': all_batch }
    return render(request, 'admin/batch.html', data)

def batch_insert(request):
    grade_id = request.Post.get('grade_id')
    subject = request.POST.get('subject')
    time = request.POST.get('time')
    description = request.POST.get('description')
    fee = request.POST.get('fee')
    module = request.POST.get('module')
    image = request.FILES.get('image')
    data = (subject, time, description, fee, module, image)
    batch_data = {'data': data}
    if batch_data:
        if len(subject)==0:
            messages.success("Subject is required")
        elif len(time)==0:
            messages.success("Time is required")
        elif len(description)==0:
            messages.success("Description is required")
        elif len(fee)==0:
            messages.success("Fee is required")
        elif len(module)==0:
            messages.success("Module is required")
        else: 
            grade = Grade.objects.get(pk=grade_id)
            batch_obj = Batch()
            batch_obj.grade_id = grade
            batch_obj.subject = subject
            batch_obj.time = time
            batch_obj.description = description
            batch_obj.fee = fee
            batch_obj.module = module
            batch_obj.image = image
            batch_obj.save()
    else:
        messages.success("Batch information inserted successfully")
    return redirect('batch')

