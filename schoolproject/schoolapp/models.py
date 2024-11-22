from django.db import models

class Guardian(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    guardian_id = models.AutoField(primary_key=True)  # Removed default=0
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    relation_to_student = models.CharField(max_length=30)
    
class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_of_birth = models.DateField(default='2000-01-01')
    gender = models.CharField(max_length=10)
    student_id = models.AutoField(primary_key=True)  # Removed default=0
    address = models.TextField(default='')  # Default to empty string
    phone_number = models.CharField(max_length=15, default='')  # Default to empty string
    email = models.EmailField()
    guardian = models.ForeignKey(Guardian, on_delete=models.SET_NULL, null=True, blank=True)  # Allow nulls

class Teacher(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_of_birth = models.DateField(default='2000-01-01')
    gender = models.CharField(max_length=10)
    employee_id = models.AutoField(primary_key=True)  # Removed default=0
    address = models.TextField(default='')  # Default to empty string
    phone_number = models.CharField(max_length=15, default='')  # Default to empty string
    email = models.EmailField()
    subject_specialization = models.ManyToManyField('Subject')

class Classroom(models.Model):
    name = models.CharField(max_length=30)
    classroom_id = models.AutoField(primary_key=True)  # Removed default=0
    grade_level = models.CharField(max_length=10)
    class_teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, blank=True)  # Allow nulls
    students = models.ManyToManyField(Student, through='Enrollment')

class Subject(models.Model):
    name = models.CharField(max_length=30)
    subject_id = models.AutoField(primary_key=True)  # Removed default=0
    code = models.CharField(max_length=10)
    description = models.TextField()
    teachers = models.ManyToManyField(Teacher)

class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    date_enrolled = models.DateField()

class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    grade = models.CharField(max_length=5)
    comments = models.TextField(default='')  # Default to empty string
    date = models.DateField()

class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=10)

class Timetable(models.Model):
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    day_of_week = models.CharField(max_length=10)
    start_time = models.TimeField()
    end_time = models.TimeField()

class Exam(models.Model):
    name = models.CharField(max_length=30)
    exam_id = models.AutoField(primary_key=True)  # Removed default=0
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    date = models.DateField()
    total_marks = models.IntegerField()

class Result(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    marks_obtained = models.IntegerField()

class Notice(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateField()
    audience = models.ManyToManyField(Classroom)

class Message(models.Model):
    sender = models.ForeignKey(Teacher, related_name='sent_messages', on_delete=models.CASCADE)
    receiver = models.ForeignKey(Guardian, related_name='received_messages', on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

class Fee(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    due_date = models.DateField()
    status = models.CharField(max_length=10)

class Payment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    payment_method = models.CharField(max_length=20)
