from django.db import models

class codePost(models.Model):
    title = models.CharField(max_length=50)
    post_dat = models.DateTimeField(auto_now=False, auto_now_add=False)
    end_Data = models.DateTimeField(auto_now=False, auto_now_add=False)
    code_exp = models.CharField(max_length=500)
    codeinput= models.CharField(max_length=200)
    codeoutput = models.CharField( max_length=200)

class sub_code(models.Model):
    user = models.CharField(max_length=50,default='')
    sub_time=models.CharField(max_length=50)
    codeTitel = models.CharField(max_length=250)
    sub_lang = models.CharField( max_length=50,default='')
    sub_data = models.CharField( max_length=500,default='') 

class userVisitData(models.Model):
    usename = models.CharField(max_length=50,default='')
    codeId = models.IntegerField()
    stTime = models.DateTimeField(auto_now=False, auto_now_add=False)

class winnerSave(models.Model):
    username = models.CharField(max_length=50)
    Title = models.CharField(max_length=100)
    Sub_time = models.CharField(max_length=50)

class testCases(models.Model):
    codeId = models.IntegerField()
    testInp = models.CharField(max_length=50,default='')
    testOut = models.CharField(max_length=50,default='')