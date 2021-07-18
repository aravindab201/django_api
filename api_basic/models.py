from django.db import models

# Create your models here.

class EmployeeModel(models.Model):
    empno = models.IntegerField()
    empname = models.CharField(max_length=100)

    def __str__(self):
        return self.empname

