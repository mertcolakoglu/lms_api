from django.urls import path
from .views import ProgressListView, CourseProgressView

urlpatterns = [
    path('progress/', ProgressListView.as_view(), name='progress-list'),
    path('courses/<int:course_id>/progress/', CourseProgressView.as_view(), name='course-progress'),
]