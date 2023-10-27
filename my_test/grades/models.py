from django.db import models

class Grade(models.Model):
    class_id = models.AutoField(primary_key=True)
    grade = models.CharField(max_length=50)
    
