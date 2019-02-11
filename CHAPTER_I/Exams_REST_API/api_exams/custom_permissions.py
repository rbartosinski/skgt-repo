from rest_framework import permissions
from .models import Exam


# custom permission class for ExamViewSet
class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):

        # allow GET, HEAD, OPTIONS methods of using data to everyone
        if request.method in permissions.SAFE_METHODS:
            return True

        # write, update or delete the data can only owner/creator exam sheet
        return obj.owner == request.user


# custom permission class for TaskViewSet
class IsOwnerExamOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):

        # allow GET, HEAD, OPTIONS methods of using data to everyone
        exam = Exam.objects.get(id=obj.exam.id)
        if request.method in permissions.SAFE_METHODS:
            return True

        # write, update or delete the data can only owner/creator exam sheet
        # where specified task is assigned
        else:
            return exam.owner == request.user
