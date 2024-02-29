# models.py

from django.db import models

class Tawassut(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=10)
    address = models.TextField()

class Kafeel(models.Model):
    number = models.IntegerField(unique=True, primary_key=True)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=10)
    address = models.TextField()
    tawassut = models.ForeignKey(Tawassut, on_delete=models.SET_NULL, null=True)
    
class Course(models.Model):
    name = models.CharField(max_length=255)

class Class(models.Model):
    name = models.CharField(max_length=255)

class Section(models.Model):
    name = models.CharField(max_length=255)

class Student(models.Model):
    admission_number = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    father_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=10)
    address = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    class_field = models.ForeignKey(Class, on_delete=models.CASCADE)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    kafeel = models.ForeignKey(Kafeel, on_delete=models.CASCADE)
    sponsoring_since = models.DateField(null=True)
   

    STATUS_CHOICES = [
        ('Active', 'Active'),
        ('Deactive', 'Deactive'),
        ('Dropped Out', 'Dropped Out'),
        ('Course Complete', 'Course Complete'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)



class Progress(models.Model):
    kafeel = models.ForeignKey(Kafeel, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    receipt_number = models.CharField(max_length=255, unique=True)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    study_report = models.TextField()
    paid_date = models.DateTimeField(auto_now_add=True)

    
# views.py
from django.shortcuts import render

def sponsor_dashboard(request, kafeel_id):
    kafeel = Kafeel.objects.get(number=kafeel_id)
    students = Student.objects.filter(kafeel=kafeel)

    context = {'kafeel': kafeel, 'students': students}
    return render(request, 'sponsor_dashboard.html', context)

def student_details(request, admission_number):
    student = Student.objects.get(admission_number=admission_number)
    progress = Progress.objects.filter(student=student)

    context = {'student': student, 'progress': progress}
    return render(request, 'student_details.html', context)
