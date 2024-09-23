# models.py
from django.db import models

class CourseForm(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    course = models.CharField(max_length=100)

    def __str__(self):
        return self.name
