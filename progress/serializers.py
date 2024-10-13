from rest_framework import serializers
from .models import Progress, LectureProgress, AssignmentProgress

class LectureProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = LectureProgress
        fields = ['lecture', 'is_completed', 'last_accessed']

class AssignmentProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssignmentProgress
        fields = ['assignment', 'is_submitted', 'score']

class ProgressSerializer(serializers.ModelSerializer):
    lecture_progress = LectureProgressSerializer(many=True, read_only=True)
    assignment_progress = AssignmentProgressSerializer(many=True, read_only=True)

    class Meta:
        model = Progress
        fields = ['id', 'student', 'course', 'last_accessed', 'completion_percentage', 'lecture_progress', 'assignment_progress']
        read_only_fields = ['student', 'course', 'completion_percentage']