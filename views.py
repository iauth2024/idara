# views.py

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Tawassut,Kafeel, Course, Class, Section, Student, Progress


def home(request):
    return render(request, 'home.html')
# kifalat/views.py


def sponsor_dashboard(request, kafeel_id):
    if request.method == 'POST':
        entered_number = request.POST.get('kafeel_number')
        entered_phone = request.POST.get('kafeel_phone')

        try:
            # Convert to integers if they are numeric fields
            entered_number = int(entered_number)
            entered_phone = int(entered_phone)

            # Check if the entered credentials are correct
            kafeel = get_object_or_404(Kafeel, number=entered_number, phone=entered_phone)

            # Fetch dashboard data for the authenticated kafeel
            # Filter students based on sponsoring_since field
            dashboard_data = Student.objects.filter(kafeel=kafeel, sponsoring_since__isnull=False)

            # Fetch related progress for each student
            for student in dashboard_data:
                student.progress_data = Progress.objects.filter(student=student)
                    
            # Pass the data to the template context
            context = {'kafeel': kafeel, 'dashboard_data': dashboard_data}
            return render(request, 'sponsor_dashboard.html', context)

        except (ValueError, Kafeel.DoesNotExist):
            return render(request, 'sponsor_dashboard_login.html', {'error_message': 'Invalid Kafeel credentials. Please try again.'})

    return render(request, 'sponsor_dashboard_login.html', {'kafeel_id': kafeel_id})



def student_details(request, admission_number):
    student = get_object_or_404(Student, admission_number=admission_number)
    progress = Progress.objects.filter(student=student)

    context = {'student': student, 'progress': progress}
    return render(request, 'student_details.html', context)

def progress_form(request, kafeel_id, admission_number):
    if request.method == 'POST':
        # Handle form submission and save progress data
        # Add your form handling logic here
        return HttpResponse("Progress data saved successfully!")

    kafeel = get_object_or_404(Kafeel, number=kafeel_id)
    student = get_object_or_404(Student, admission_number=admission_number)

    context = {'kafeel': kafeel, 'student': student}
    return render(request, 'progress_form.html', context)

