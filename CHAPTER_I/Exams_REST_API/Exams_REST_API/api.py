from rest_framework.routers import DefaultRouter
from api_exams.views import ExamViewSet, TaskViewSet
from rest_framework_extensions.routers import NestedRouterMixin


class NestedDefaultRouter(NestedRouterMixin, DefaultRouter):
    pass


router = NestedDefaultRouter()

authors_router = router.register('exams', ExamViewSet)
authors_router.register(
    'tasks', TaskViewSet,
    base_name='exams-tasks',
    parents_query_lookups=['exam'])

