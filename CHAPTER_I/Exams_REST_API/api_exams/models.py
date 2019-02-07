from django.db import models


# define model with relation data structure of exams sheets
class Exam(models.Model):
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=256)
    date = models.DateField(null=True)
    final_grade = models.IntegerField(null=True)
    owner = models.ForeignKey('auth.User', related_name='exams', on_delete=models.CASCADE)

    # set the field to 'stringify' object/instance when it will be displayed eg. in panel admin
    def __str__(self):
        return self.title


# define model with relation data structure of task of exams
class Task(models.Model):
    description = models.CharField(max_length=256)
    exam = models.ForeignKey(Exam, null=True, on_delete=models.SET_NULL)
    points = models.IntegerField(null=True)

    # set the field to 'stringify' object/instance when it will be displayed eg. in panel admin
    def __str__(self):
        return self.description
