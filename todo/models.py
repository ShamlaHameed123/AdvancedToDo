from django.db import models
from django.contrib.auth.models import User
from django import forms
# Create your models here.


class Task(models.Model):
    PRIORITY_CHOICES =(
        ("L", "Low"),
        ("M", "Medium"),
        ("H", "High"),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField(max_length=1000, blank=False)
    completed = models.BooleanField(default=False)
    due_date = models.DateField()
    priority = models.CharField(max_length=1, choices=PRIORITY_CHOICES)
