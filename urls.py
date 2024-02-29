# kifalat/urls.py

from django.urls import path
from .views import sponsor_dashboard, student_details, progress_form, home

urlpatterns = [
     path('', home, name='home'),
    path('sponsor_dashboard/<int:kafeel_id>/', sponsor_dashboard, name='sponsor_dashboard'),
    path('student_details/<int:admission_number>/', student_details, name='student_details'),
    path('progress_form/<int:kafeel_id>/<int:admission_number>/', progress_form, name='progress_form'),
    path('home/', home, name='home'),
    # Add more paths for other views as needed
]
