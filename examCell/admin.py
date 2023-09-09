from django.contrib import admin
from .models import Result


@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ('id', 'uname', 'time', 'totalQuestion', 'rightAnswer', 'questionId')
