from django.db import models
from django.conf import settings
from courses.models import Course, Enrollment
from metarials.models import Lecture, Assignment

class Progress(models.Model):
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='progress')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='student_progress')
    last_accessed = models.DateTimeField(auto_now=True)
    completion_percentage = models.FloatField(default=0.0)

    class Meta:
        unique_together = ['student', 'course']

    def __str__(self):
        return f"{self.student.username}'s progress in {self.course.title}"

class LectureProgress(models.Model):
    progress = models.ForeignKey(Progress, on_delete=models.CASCADE, related_name='lecture_progress')
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE)
    is_completed = models.BooleanField(default=False)
    last_accessed = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ['progress', 'lecture']

class AssignmentProgress(models.Model):
    progress = models.ForeignKey(Progress, on_delete=models.CASCADE, related_name='assignment_progress')
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    is_submitted = models.BooleanField(default=False)
    score = models.FloatField(null=True, blank=True)

    class Meta:
        unique_together = ['progress', 'assignment']