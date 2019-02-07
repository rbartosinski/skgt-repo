from django.contrib import admin
from .models import Exam, Task


# add access to exams and tasks models in panel admin
admin.site.register(Exam)
admin.site.register(Task)
