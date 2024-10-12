from django.urls import path
from .views import LectureListCreateView, LectureRetrieveUpdateDestroyView, AssignmentListCreateView, AssignmentRetrieveUpdateDestroyView, SubmissionCreateView, SubmissionRetrieveUpdateView

urlpatterns = [
    path('courses/<int:course_id>/lectures/', LectureListCreateView.as_view(), name='lecture-list-create'),
    path('lectures/<int:pk>/', LectureRetrieveUpdateDestroyView.as_view(), name='lecture-detail'),
    path('lectures/<int:lecture_id>/assignments/', AssignmentListCreateView.as_view(), name='assignment-list-create'),
    path('assignments/<int:pk>/', AssignmentRetrieveUpdateDestroyView.as_view(), name='assignment-detail'),
    path('assignments/<int:assignment_id>/submit/', SubmissionCreateView.as_view(), name='submission-create'),
    path('submissions/<int:pk>/', SubmissionRetrieveUpdateView.as_view(), name='submission-detail'),
]