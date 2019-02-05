from rest_framework_extensions.mixins import NestedViewSetMixin
from .models import Exam, Task
from .serializers import ExamSerializer, TaskSerializer
from rest_framework.viewsets import ModelViewSet


class ExamViewSet(ModelViewSet):
    serializer_class = ExamSerializer
    queryset = Exam.objects.all()


class TaskViewSet(NestedViewSetMixin, ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

