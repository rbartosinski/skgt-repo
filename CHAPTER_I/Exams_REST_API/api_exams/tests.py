from django.test import TestCase
from rest_framework.test import APIRequestFactory, force_authenticate
from django.contrib.auth.models import User
from .models import Exam
from .views import ExamViewSet


class TestViewSetCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create(username="test_user", password="test_password")
        cls.exam_1 = Exam.objects.create(title="First", description="My first exam", owner=cls.user)
        cls.exam_2 = Exam.objects.create(title="Second", description="My second exam", owner=cls.user)

    def test_get_retrieve(self):
        request = APIRequestFactory().get("")
        exam_detail = ExamViewSet.as_view(actions={'get': 'retrieve'})
        response = exam_detail(request, pk=self.exam_1.pk)
        self.assertEqual(response.status_code, 200)

