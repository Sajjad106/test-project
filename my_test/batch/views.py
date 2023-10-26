from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages 
from .models import Batch

def batch(request):
    data = Batch.objects.all()
    batch_data = {'data': data}
    return render(request, 'admin/batch.html', batch_data)

def batch_insert(request):
    grade = request.POST.get('grade')
    subject = request.POST.get('subject')
    time = request.POST.get('time')
    description = request.POST.get('description')
    fee = request.POST.get('fee')
    module = request.POST.get('module')
    image = request.FILES.get('image')
    data = (subject, time, description, fee, module, image)
    batch_data = {'data': data}
    if batch_data:
        if len(grade)==0:
            messages.success("Class is required")
        elif len(subject)==0:
            messages.success("Subject is required")
        elif len(time)==0:
            messages.success("Time is required")
        elif len(description)==0:
            messages.success("Description is required")
        elif len(fee)==0:
            messages.success("Fee is required")
        elif len(module)==0:
            messages.success("Module is required")
        # elif len(image)==0:
        #     messages.success("Image is required")
        else: 
            batch_obj = Batch()
            batch_obj.grade = grade
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

