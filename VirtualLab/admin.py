from django.contrib import admin
from .models import userVisitData, winnerSave, testCases, sub_code, codePost


# Register your models here.
@admin.register(userVisitData)
class userVisitDataAdmin(admin.ModelAdmin):
    list_display = ("usename", "codeId", "stTime")

@admin.register(winnerSave)
class winnerSaveAdmin(admin.ModelAdmin):
    list_display = ("username", "Title", "Sub_time")

@admin.register(testCases)
class testCasesAdmin(admin.ModelAdmin):
    list_display = ("codeId", "testInp", "testOut")

@admin.register(sub_code)
class sub_codeAdmin(admin.ModelAdmin):
    list_display = ("user", "sub_time", "codeTitel", "sub_lang", "sub_data")

@admin.register(codePost)
class codePostAdmin(admin.ModelAdmin):
    list_display = ("title", "post_dat", "end_Data", "code_exp", "codeinput", "codeoutput")
