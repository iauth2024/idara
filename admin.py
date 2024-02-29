# kifalat/admin.py

from django.contrib import admin
from .models import Tawassut, Kafeel, Course, Class, Section, Student, Progress

@admin.register(Tawassut)
class TawassutAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Tawassut._meta.fields]

@admin.register(Kafeel)
class KafeelAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Kafeel._meta.fields]

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Course._meta.fields]

@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Class._meta.fields]

@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Section._meta.fields]

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Student._meta.fields]

@admin.register(Progress)
class ProgressAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Progress._meta.fields]
