from django.contrib import admin
from .models import Lesson, Problem, Attempt


@admin.register(Lesson)
class LessonModelAdmin(admin.ModelAdmin):
    list_display = ['short_title', 'count_showers', 'count_enders']

@admin.register(Problem)
class ProblemModelAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Attempt)
class AttemptModelAdmin(admin.ModelAdmin):
    list_display = ['author', 'status', 'time']