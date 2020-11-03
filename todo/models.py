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
    title = models.CharField(db_column='title', max_length=100, blank=False)
    content = models.TextField(db_column='description', max_length=1000, blank=False)
    completed = models.BooleanField(default=False)
    due_date = models.DateField()
    priority = models.CharField(max_length=1, choices=PRIORITY_CHOICES)
