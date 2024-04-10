from django.db import models

# Create your models here.

class Tasks(models.model):
    Title = models.CharField(max_length=200, null= True)

