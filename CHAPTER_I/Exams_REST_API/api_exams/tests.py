"""
PERMANENT ERROR with every tests
---
django.core.exceptions.ImproperlyConfigured:
Requested setting REST_FRAMEWORK, but settings
are not configured. You must either define
the environment variable DJANGO_SETTINGS_MODULE
or call settings.configure() before accessing settings.
"""

from django.test import TestCase
from rest_framework.test import APIRequestFactory
from api_exams.models import Exam
from api_exams.views import ExamViewSet


class TestViewSetCase(TestCase):

    def test_view_set(self):
        pass
        # request = APIRequestFactory().get("")
        # exam_detail = ExamViewSet.as_view(actions={'get': 'retrieve'})
        # exam = Exam.objects.create(title="First", description="My first exam")
        # response = exam_detail(request, pk=exam.pk)
        # self.assertEqual(response.status_code, 200)
