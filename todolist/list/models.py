from django.db import models
from django.utils import timezone


# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200)
    is_done = models.BooleanField(default=False)

   
    
    



    
    
    
     
    
