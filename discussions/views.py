from rest_framework import generics, permissions
from .models import Discussion, Comment
from .serializers import DiscussionSerializer, CommentSerializer
from courses.models import Course
from django.shortcuts import get_object_or_404
from core.permissions import IsEnrolledOrInstructor, IsDiscussionOrCommentCreatorOrReadOnly


# Create your views here.

class DiscussionListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = DiscussionSerializer
    permission_classes = [permissions.IsAuthenticated, IsEnrolledOrInstructor]

    def get_queryset(self):
        course = get_object_or_404(Course, pk=self.kwargs['course_id'])
        if self.request.user == course.instructor:
            return Discussion.objects.filter(course=course)
        return Discussion.objects.filter(course=course, created_by=self.request.user)

    def perform_create(self, serializer):
        course = get_object_or_404(Course, pk=self.kwargs['course_id'])
        serializer.save(course=course, created_by=self.request.user)
    
class DiscussionRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Discussion.objects.all()
    serializer_class = DiscussionSerializer
    permission_classes = [permissions.IsAuthenticated, IsDiscussionOrCommentCreatorOrReadOnly]

class CommentListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated, IsEnrolledOrInstructor]

    def get_queryset(self):
        discussion = get_object_or_404(Discussion, pk=self.kwargs['discussion_id'])
        return Comment.objects.filter(discussion=discussion)

    def perform_create(self, serializer):
        discussion = get_object_or_404(Discussion, pk=self.kwargs['discussion_id'])
        serializer.save(discussion=discussion, created_by=self.request.user)

class CommentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated, IsDiscussionOrCommentCreatorOrReadOnly]