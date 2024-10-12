from rest_framework import serializers
from .models import Lecture, Assignment, Submission

class LectureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecture
        fields = ['id', 'title', 'content', 'order', 'video_url', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']
    
class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = ['id', 'title', 'description', 'due_date', 'max_points', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']
    
class SubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submission
        fields = ['id', 'assignment', 'student', 'submitted_at', 'content', 'score']
        read_only_fields = ['submitted_at', 'score']
    
class SubmissionUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submission
        fields = ['score']