from rest_framework import generics, permissions
from .models import Progress
from .serializers import ProgressSerializer
from courses.models import Course
from core.permissions import IsEnrolled

class ProgressListView(generics.ListAPIView):
    serializer_class = ProgressSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Progress.objects.filter(student=self.request.user)

class CourseProgressView(generics.RetrieveAPIView):
    serializer_class = ProgressSerializer
    permission_classes = [permissions.IsAuthenticated, IsEnrolled]

    def get_object(self):
        course = Course.objects.get(pk=self.kwargs['course_id'])
        return Progress.objects.get(student=self.request.user, course=course)