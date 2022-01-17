from django.db import models
from django.utils import timezone


# Create your models here.


class Department(models.Model):
    full_name = models.TextField()
    short_name = models.CharField(max_length=100)
    phone = models.TextField(null=True)


class Person(models.Model):
    first_name = models.CharField(max_length=200, default="anonymous")
    last_name = models.CharField(max_length=200, default="anonymous")
    patronymic = models.CharField(max_length=200, default="anonymous")
    birth_date = models.DateField(default=timezone.now)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)

