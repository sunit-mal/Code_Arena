from django.db import models

class ExamQuestions(models.Model):
    examId = models.IntegerField()
    question = models.CharField(max_length=500)

    option1 = models.CharField(max_length=50)
    option2 = models.CharField(max_length=50)
    option3 = models.CharField(max_length=50)
    option4 = models.CharField(max_length=50)

    answer = models.CharField(max_length=2)


class ExamDetails(models.Model):
    Title = models.CharField(max_length=500)

class Result(models.Model):
    questionId = models.IntegerField()
    uname = models.CharField(max_length=50)
    time = models.DateField(auto_now=False, auto_now_add=False)
    totalQuestion = models.IntegerField()
    rightAnswer = models.IntegerField()