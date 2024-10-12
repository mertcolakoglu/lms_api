from rest_framework import serializers
from .models import Course, Enrollment
from users.serializers import UserSerializer

class CourseSerializer(serializers.ModelSerializer):
    #instructor = UserSerializer(read_only=True)
    instructor = serializers.StringRelatedField( read_only=True, source='instructor.username')

    class Meta:
        model = Course
        fields = '__all__'
    

class CourseCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ("title", "description", "start_date", "end_date", "category", "max_students")


class EnrollmentSerializer(serializers.ModelSerializer):
    #student = UserSerializer(read_only=True)
    student = serializers.StringRelatedField(read_only=True, source='student.username')
    #course = CourseSerializer(read_only=True)
    course = serializers.StringRelatedField(read_only=True, source='course.title')

    class Meta:
        model = Enrollment
        fields = '__all__'
    

class EnrollmentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = ('course', 'status')
    