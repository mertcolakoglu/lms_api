from django.db.models.signals import post_save
from django.dispatch import receiver
from courses.models import Enrollment
from metarials.models import Submission, Assignment
from .models import Progress, LectureProgress, AssignmentProgress

@receiver(post_save, sender=Enrollment)
def create_progress(sender, instance, created, **kwargs):
    if created:
        progress = Progress.objects.create(student=instance.student, course=instance.course)
        for lecture in instance.course.lectures.all():
            LectureProgress.objects.create(progress=progress, lecture=lecture)
        for assignment in Assignment.objects.filter(lecture__course=instance.course):
            AssignmentProgress.objects.create(progress=progress, assignment=assignment)

@receiver(post_save, sender=Submission)
def update_assignment_progress(sender, instance, **kwargs):
    progress = Progress.objects.get(student=instance.student, course=instance.assignment.lecture.course)
    assignment_progress = AssignmentProgress.objects.get(progress=progress, assignment=instance.assignment)
    assignment_progress.is_submitted = True
    assignment_progress.score = instance.score
    assignment_progress.save()

    total_assignments = AssignmentProgress.objects.filter(progress=progress).count()
    completed_assignments = AssignmentProgress.objects.filter(progress=progress, is_submitted=True).count()
    total_lectures = LectureProgress.objects.filter(progress=progress).count()
    completed_lectures = LectureProgress.objects.filter(progress=progress, is_completed=True).count()

    total_items = total_assignments + total_lectures
    completed_items = completed_assignments + completed_lectures

    progress.completion_percentage = (completed_items / total_items) * 100 if total_items > 0 else 0
    progress.save()