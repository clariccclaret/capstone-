from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import (
    Guardian, Student, Teacher, Classroom, Subject, Enrollment,
    Grade, Attendance, Timetable, Exam, Result, Notice, Message, Fee, Payment
)
from .serializers import (
    GuardianSerializer, StudentSerializer, TeacherSerializer, ClassroomSerializer,
    SubjectSerializer, EnrollmentSerializer, GradeSerializer, AttendanceSerializer,
    TimetableSerializer, ExamSerializer, ResultSerializer, NoticeSerializer,
    MessageSerializer, FeeSerializer, PaymentSerializer
)

class GuardianViewSet(ModelViewSet):
    queryset = Guardian.objects.all()
    serializer_class = GuardianSerializer

class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class TeacherViewSet(ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class ClassroomViewSet(ModelViewSet):
    queryset = Classroom.objects.all()
    serializer_class = ClassroomSerializer

class SubjectViewSet(ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

class EnrollmentViewSet(ModelViewSet):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer

class GradeViewSet(ModelViewSet):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer

class AttendanceViewSet(ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer

class TimetableViewSet(ModelViewSet):
    queryset = Timetable.objects.all()
    serializer_class = TimetableSerializer

class ExamViewSet(ModelViewSet):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer

class ResultViewSet(ModelViewSet):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer

class NoticeViewSet(ModelViewSet):
    queryset = Notice.objects.all()
    serializer_class = NoticeSerializer

class MessageViewSet(ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

class FeeViewSet(ModelViewSet):
    queryset = Fee.objects.all()
    serializer_class = FeeSerializer

class PaymentViewSet(ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

def home(request):
    return render(request, 'home.html')
