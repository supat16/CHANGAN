from django.db import models
from django.contrib.auth.models import User

class Status(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Position(models.Model):
    name = models.CharField(max_length=50)
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Department(models.Model):
    name = models.CharField(max_length=50)
    manager = models.ForeignKey('Employee', on_delete=models.SET_NULL, null=True, blank=True, related_name='managed_department')

    def __str__(self):
        return self.name

class Employee(models.Model):
    name = models.CharField(max_length=50)
    address = models.TextField()
    manager = models.BooleanField(default=False)
    status = models.ForeignKey('Status', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='employee_images/' ,null=True, blank=True)
    position = models.ForeignKey('Position', on_delete=models.CASCADE)
    department = models.ForeignKey('Department', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
