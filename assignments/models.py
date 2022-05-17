from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# class Student(models.Model):
#     user = models.OneToOneField(
#     User,
#     on_delete = models.CASCADE,
#     primary_key = True`
#     )
#     name = models.TextField(default="", blank=True)
#     school = models.CharField(max_length=100, default="",blank=True)

class Assignment(models.Model):
    userAssignments = models.ForeignKey(User, on_delete=models.CASCADE)
    # assignedDate = models.DateTimeField('date assigned')
    name = models.TextField(default="", blank=True)
    dueDate = models.DateTimeField('date due')
    complete = models.BooleanField(default=False)
