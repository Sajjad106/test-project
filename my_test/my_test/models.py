from django.db import models
from django import forms
class StudentEntry(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    grade = models.PositiveIntegerField()
    mothers_name = models.CharField(max_length=100)
    fathers_name = models.CharField(max_length=100)
    guardians_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(default='1988-01-01')
    contact_no = models.CharField(max_length=20)
    present_address = models.TextField(max_length=100)
    permanent_address = models.TextField(max_length=100)
    
    
    
    