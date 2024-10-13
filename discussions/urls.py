from django.urls import path
from .views import DiscussionListCreateAPIView, DiscussionRetrieveUpdateDestroyAPIView, CommentListCreateAPIView, CommentRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('courses/<int:course_id>/discussions/', DiscussionListCreateAPIView.as_view(), name='discussion-list'),
    path('discussions/<int:pk>/', DiscussionRetrieveUpdateDestroyAPIView.as_view(), name='discussion-detail'),
    path('discussions/<int:discussion_id>/comments/', CommentListCreateAPIView.as_view(), name='comment-list'),
    path('comments/<int:pk>/', CommentRetrieveUpdateDestroyAPIView.as_view(), name='comment-detail'),
]