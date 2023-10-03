from django.db import models


class StudentEntry(models.Model):
    student_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    grade = models.IntegerField(max_length=12)
    mothers_name = models.CharField(max_length=100)
    fathers_name = models.CharField(max_length=100)
    guardians_name = models.CharField(max_length=100)
    date_of_birth = models.CharField(default='1988-01-01', max_length=10000000)
    contact_no = models.IntegerField(max_length=11)
    present_address = models.TextField(max_length=100)
    permanent_address = models.TextField(max_length=100)
    
    
    
    