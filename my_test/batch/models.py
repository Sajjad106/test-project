from django.db import models
from grades.models import Grade

class Batch(models.Model):
    batch_id = models.AutoField(primary_key=True)
    class_id = models.ForeignKey(Grade, on_delete=models.CASCADE, default=True)
    subject = models.CharField(max_length=100)
    time = models.CharField(max_length=50)
    description = models.TextField()
    fee = models.IntegerField()
    module = models.TextField(max_length=11)
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    
