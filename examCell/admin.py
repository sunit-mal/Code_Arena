from django.contrib import admin
from .models import Result, ExamDetails, ExamQuestions


@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ('id', 'uname', 'time', 'totalQuestion', 'rightAnswer', 'questionId')

@admin.register(ExamDetails)
class ExamDetailsAdmin(admin.ModelAdmin):
    list_display = ('id', 'Title')

@admin.register(ExamQuestions)
class ExamQuestionsAdmin(admin.ModelAdmin):
    list_display = ('id', 'examId', 'question', 'option1', 'option2', 'option3', 'option4', 'answer')