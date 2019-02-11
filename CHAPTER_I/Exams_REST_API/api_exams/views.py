from rest_framework.filters import OrderingFilter
from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet
from rest_framework_extensions.mixins import NestedViewSetMixin
from .custom_permissions import IsOwnerOrReadOnly, IsOwnerExamOrReadOnly
from .models import Exam, Task
from .serializers import ExamSerializer, TaskSerializer


# 'api/exams' REST endpoint backend
class ExamViewSet(ModelViewSet):

    # general and custom access permissions
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    # define correct JSON serializer and required declaration of queryset
    serializer_class = ExamSerializer
    queryset = Exam.objects.all()

    # define filters to get the data
    filter_backends = (OrderingFilter,)
    ordering_fields = ('owner', 'final_grade', 'date', 'title')

    # overwrite create/POST method action to select logged user as owner
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


# 'api/tasks' REST endpoint backend
class TaskViewSet(NestedViewSetMixin, ModelViewSet):

    # general and custom access permissions
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerExamOrReadOnly,)

    # define correct JSON serializer and required declaration of queryset
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
