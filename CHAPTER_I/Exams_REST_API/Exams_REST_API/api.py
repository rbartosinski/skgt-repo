from rest_framework.routers import DefaultRouter
from api_exams.views import ExamViewSet, TaskViewSet
from rest_framework_extensions.routers import NestedRouterMixin


# nested API routing needed to correct show relation structure of the db
class NestedDefaultRouter(NestedRouterMixin, DefaultRouter):
    pass


router = NestedDefaultRouter()

exams_router = router.register('exams', ExamViewSet)
exams_router.register(
    'tasks', TaskViewSet,
    base_name='exams-tasks',
    parents_query_lookups=['exam'])

