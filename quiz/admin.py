from django.contrib import admin
from .models import Quiz, Question, UserQuizAttempt, AttemptRecord

# Register your models here.

admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(UserQuizAttempt)
admin.site.register(AttemptRecord)