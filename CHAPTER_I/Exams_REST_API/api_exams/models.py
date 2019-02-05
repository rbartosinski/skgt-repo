from django.contrib.auth.models import User
from django.db import models


class Exam(models.Model):
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=256)
    date = models.DateField(null=True)
    owner = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title


class Task(models.Model):
    description = models.CharField(max_length=256)
    exam = models.ForeignKey(Exam, null=True, on_delete=models.SET_NULL)
    points = models.IntegerField(null=True)

    def __str__(self):
        return self.description


