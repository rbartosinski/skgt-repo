from django.contrib.auth.models import User
from django.db import models


class Task(models.Model):
    description = models.CharField(max_length=256)
    points = models.IntegerField()

    def __str__(self):
        return self.description


class Exam(models.Model):
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=256)
    date = models.DateField(null=True)
    task = models.ForeignKey(Task, null=True,
                             on_delete=models.SET_NULL,
                             related_name='exams_task')
    owner = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title
