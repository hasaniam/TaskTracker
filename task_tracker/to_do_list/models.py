from django.db import models

# Create your models here.

class Tasks(models.Model):
    #User = models.ForeignKey()
    Title = models.CharField(max_length=200, null=True)
    Date = models.DateField(null=True)
    Time = models.TimeField(null=True)
