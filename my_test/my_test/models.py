from django.db import models
class StudentEntry(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    grade = models.IntegerField(max_length=12, null=True)
    mothers_name = models.CharField(max_length=100, default='Unknown')
    fathers_name = models.CharField(max_length=100, default='Unknown')
    gurdians_name = models.CharField(max_length=100, default='Unknown')
    date_of_birth = models.DateField(default='1988-01-01', blank=True)
    contact_no = models.CharField(max_length=20, default='N/A')
    peresent_adress = models.TextField(max_length=100, default='N/A', null=False)
    permanent_adress = models.TextField(max_length=100, default='N/A', null=False)
    
    
    
    