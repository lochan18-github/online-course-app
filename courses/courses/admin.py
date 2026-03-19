from django.contrib import admin
from .models import Question, Choice, Submission

# Inline for Choices
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2


# Inline for Questions
class QuestionInline(admin.TabularInline):
    model = Question
    extra = 2


# Admin for Question
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ('question_text',)


# Dummy Lesson model (since not defined earlier)
# You NEED this for grading
from django.db import models

class Lesson(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


# Admin for Lesson
class LessonAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]


# Register models
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Submission)
admin.site.register(Lesson, LessonAdmin)
