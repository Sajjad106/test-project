from django.db import models
from my_test.models import StudentEntry

class batch(models.Model):
    batch_id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(StudentEntry, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    Time = models.CharField(max_length=50)
    no_of_student = models.IntegerField()
    description = models.TextField()
    fee = models.IntegerField()
    discount = models.IntegerField()
    module = models.TextField(max_length=11)
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    
