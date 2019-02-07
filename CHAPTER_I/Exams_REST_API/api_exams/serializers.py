from rest_framework import serializers
from .models import Task, Exam


# changing the data from db model Exam to JSON
class ExamSerializer(serializers.ModelSerializer):

    class Meta:
        # set correct model form the db and fields to serialize
        model = Exam
        fields = ('id', 'title', 'description', 'date', 'final_grade', 'owner')

        # define field 'owner' as read only
        owner = serializers.ReadOnlyField(source='owner.username')


# changing the data from db model Task to JSON
class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        # set correct model form the db and fields to serialize
        model = Task
        fields = ('id', 'description', 'points', 'exam')

        # define field 'exam' as read only
        exam = serializers.ReadOnlyField(source='exam.title')
