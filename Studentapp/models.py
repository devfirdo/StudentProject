from django.db import models

class Studenttable(models.Model):
    StudentName = models.CharField(max_length = 50)
    Address = models.TextField()
    Age = models.IntegerField()
    Email = models.EmailField(max_length = 100)
    JoiningDate = models.DateField()
    Qualification = models.CharField(max_length=100)
    Gender = models.CharField(max_length=100)
    MobileNumber = models.CharField(max_length=11)
