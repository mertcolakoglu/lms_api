from rest_framework import permissions
from courses.models import Enrollment
from courses.models import Course
from metarials.models import Lecture

class IsInstructorOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.user_type == 'instructor'

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.instructor == request.user


class IsEnrolled(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.student == request.user
    

class IsEnrolledOrInstructor(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return (
            Enrollment.objects.filter(student=request.user, course=obj.lecture.course, status='active').exists() or
            obj.lecture.course.instructor == request.user
        )

class IsInstructorForSubmission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.assignment.lecture.course.instructor == request.user

class IsSubmissionOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.student == request.user
    
class IsCourseInstructor(permissions.BasePermission):
    def has_permission(self, request, view):
        course_id = view.kwargs.get('course_id')
        if course_id:
            course = Course.objects.get(pk=course_id)
            return course.instructor == request.user
        return False
    

class IsLectureInstructor(permissions.BasePermission):
    def has_permission(self, request, view):
        lecture_id = view.kwargs.get('lecture_id')
        if lecture_id:
            lecture = Lecture.objects.get(pk=lecture_id)
            return lecture.course.instructor == request.user
        return False

from rest_framework import permissions

class IsDiscussionOrCommentCreatorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.created_by == request.user