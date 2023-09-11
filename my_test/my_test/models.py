from django.db import models
class StudentEntry(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    grade = models.IntegerField(max_length=12)
    mothers_name = models.CharField(max_length=100)
    fathers_name = models.CharField(max_length=100)
    gurdians_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(default='1988-01-01')
    contact_no = models.CharField(max_length=20)
    peresent_adress = models.TextField(max_length=100)
    permanent_adress = models.TextField(max_length=100 )
    
    
    
    