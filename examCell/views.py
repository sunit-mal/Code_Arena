from django.shortcuts import render, HttpResponseRedirect, HttpResponse
import datetime
import os
from subprocess import Popen, PIPE
from django.contrib import messages
from django.utils import timezone
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from .models import ExamDetails, ExamQuestions, Result
from openpyxl import Workbook
from openpyxl.writer.excel import save_virtual_workbook


def examInterface(request):
    availableQuestions = ExamDetails.objects.all()
    return render(request, 'ExamInterface.html', {'question': availableQuestions})


def StartExam(request, id):
    if request.user.is_authenticated:
        if (Result.objects.filter(questionId=id, uname=request.user.username).exists() == False):
            title = ExamDetails.objects.get(pk=id).Title
            question = ExamQuestions.objects.filter(examId=id)
            return render(request, 'examPage.html', {'Questions': question, 'id': id, 'title': title})
        else:
            return HttpResponseRedirect('/exam/')
    return HttpResponseRedirect('/login/')


def showResult(request, id):
    question = ExamQuestions.objects.filter(examId=id)
    count = 0
    total = 0
    if request.method == 'POST':
        for ques in question:
            total = total+1
            data = request.POST[f'{ques.id}']
            if data == ques.answer:
                count = count+1

    uname = request.user.username
    time = datetime.datetime.now()
    data = Result(uname=uname, time=time,
                  totalQuestion=total, rightAnswer=count, questionId=id)
    data.save()
    return HttpResponseRedirect('/exam/')


def examEntry(request):
    availableQuestions = ExamDetails.objects.all().order_by('id').reverse()
    return render(request, 'examEntry.html', {'questions': availableQuestions})


def newQuestionEntry(request):
    if request.method == 'POST':
        title = request.POST['title']
        data = ExamDetails(Title=title)
        data.save()
        question = ExamDetails.objects.get(Title=title)
        return HttpResponseRedirect(f'/QuestionEntry/{question.pk}')
    return HttpResponseRedirect("/examSet/")


def DeleteQuestion(request, id):
    question = ExamDetails.objects.get(pk=id)
    question.delete()
    details = ExamQuestions.objects.filter(examId=id)
    for data in details:
        data.delete()
    return HttpResponseRedirect("/examSet/")


def QuestionEntry(request, id):
    return render(request, 'QuestionEntry.html', {'questionId': id})


def saveQuestion(request, id):
    if request.method == 'POST':
        question = request.POST['question']
        option1 = request.POST['A']
        option2 = request.POST['B']
        option3 = request.POST['C']
        option4 = request.POST['D']
        answer = request.POST['Ans']

        data = ExamQuestions(examId=id, question=question, option1=option1,
                             option2=option2, option3=option3, option4=option4, answer=answer)
        data.save()

    return HttpResponseRedirect(f'/QuestionEntry/{id}')


def showResultData(request, id):
    results = Result.objects.filter(questionId=id)
    return render(request, 'result.html', {'result': results, 'id': id})


def generate_excel(request, id):
    return HttpResponseRedirect("/")
#     # Create a new workbook and add a worksheet
#     workbook = Workbook()
#     worksheet = workbook.active

#     # Add some sample data to the worksheet
#     worksheet['A1'] = 'User Name'
#     worksheet['B1'] = 'Submission Time'
#     worksheet['C1'] = 'Right Answer'
#     worksheet['D1'] = 'Percentage'

#     results = Result.objects.filter(questionId=id)
#     i = 2
#     questionPaperName = ''
#     for data in results:
#         worksheet[f'A{i}'] = data.uname
#         worksheet[f'B{i}'] = str(data.time)
#         worksheet[f'C{i}'] = data.rightAnswer
#         worksheet[f'D{i}'] = f'{(data.rightAnswer/data.totalQuestion)*100}%'
#         i = i+1
#         questionPaperName = ExamDetails.objects.get(id=data.questionId).Title

#     # Create a response with the Excel file
#     response = HttpResponse(
#         save_virtual_workbook(workbook),
#         content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
#     )
#     response['Content-Disposition'] = f'attachment; filename="{questionPaperName}.xlsx"'
#     return response
