from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    GuardianViewSet, StudentViewSet, TeacherViewSet, ClassroomViewSet,
    SubjectViewSet, EnrollmentViewSet, GradeViewSet, AttendanceViewSet,
    TimetableViewSet, ExamViewSet, ResultViewSet, NoticeViewSet,
    MessageViewSet, FeeViewSet, PaymentViewSet,
)

router = DefaultRouter()
router.register(r'guardians', GuardianViewSet)
router.register(r'students', StudentViewSet)
router.register(r'teachers', TeacherViewSet)
router.register(r'classrooms', ClassroomViewSet)
router.register(r'subjects', SubjectViewSet)
router.register(r'enrollments', EnrollmentViewSet)
router.register(r'grades', GradeViewSet)
router.register(r'attendances', AttendanceViewSet)
router.register(r'timetables', TimetableViewSet)
router.register(r'exams', ExamViewSet)
router.register(r'results', ResultViewSet)
router.register(r'notices', NoticeViewSet)
router.register(r'messages', MessageViewSet)
router.register(r'fees', FeeViewSet)
router.register(r'payments', PaymentViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),  # Include the router's URLs
]
