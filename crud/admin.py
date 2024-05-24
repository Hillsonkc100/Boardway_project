from django.contrib import admin
from .models import Student, StudentProfile, ClassRoom
# Register your models here.

admin.site.register(Student)
admin.site.register(StudentProfile)
admin.site.register(ClassRoom)