from django.db import models

# Create your models here.

#student registration:
class Future(models.Model):
    Name = models.CharField(max_length=50)
    Email = models.EmailField()
    Aim = models.CharField(max_length=50)
    Date = models.DateField(max_length=50)
