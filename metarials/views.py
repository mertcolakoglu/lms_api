from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import Lecture, Assignment, Submission
from .serializers import LectureSerializer, AssignmentSerializer, SubmissionSerializer, SubmissionUpdateSerializer
from core.permissions import IsEnrolledOrInstructor, IsInstructorForSubmission, IsSubmissionOwner, IsLectureInstructor, IsCourseInstructor
from courses.models import Course

class LectureListCreateView(generics.ListCreateAPIView):
    serializer_class = LectureSerializer
    permission_classes = [permissions.IsAuthenticated, IsCourseInstructor]

    def get_queryset(self):
        course = Course.objects.get(pk=self.kwargs['course_id'])
        if self.request.user == course.instructor:
            return Lecture.objects.filter(course=course)
        return Lecture.objects.filter(course=course, course__enrollments__student=self.request.user, course__enrollments__status='active')

    def perform_create(self, serializer):
        course = Course.objects.get(pk=self.kwargs['course_id'])
        serializer.save(course=course)

class LectureRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lecture.objects.all()
    serializer_class = LectureSerializer
    permission_classes = [permissions.IsAuthenticated, IsEnrolledOrInstructor]

class AssignmentListCreateView(generics.ListCreateAPIView):
    serializer_class = AssignmentSerializer
    permission_classes = [permissions.IsAuthenticated, IsLectureInstructor]

    def get_queryset(self):
        lecture = Lecture.objects.get(pk=self.kwargs['lecture_id'])
        if self.request.user == lecture.course.instructor:
            return Assignment.objects.filter(lecture=lecture)
        return Assignment.objects.filter(
            lecture=lecture,
            lecture__course__enrollments__student=self.request.user,
            lecture__course__enrollments__status='active'
        )

    def perform_create(self, serializer):
        lecture = Lecture.objects.get(pk=self.kwargs['lecture_id'])
        serializer.save(lecture=lecture)

class AssignmentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer
    permission_classes = [permissions.IsAuthenticated, IsEnrolledOrInstructor]

class SubmissionCreateView(generics.CreateAPIView):
    serializer_class = SubmissionSerializer
    permission_classes = [permissions.IsAuthenticated, IsEnrolledOrInstructor]

    def perform_create(self, serializer):
        assignment = Assignment.objects.get(pk=self.kwargs['assignment_id'])
        serializer.save(assignment=assignment, student=self.request.user)

class SubmissionRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Submission.objects.all()
    permission_classes = [permissions.IsAuthenticated, IsSubmissionOwner|IsInstructorForSubmission]

    def get_serializer_class(self):
        if self.request.method == 'PUT' and self.request.user == self.get_object().assignment.lecture.course.instructor:
            return SubmissionUpdateSerializer
        return SubmissionSerializer