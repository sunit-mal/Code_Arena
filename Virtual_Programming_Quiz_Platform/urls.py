from django.contrib import admin
from django.urls import path
from VirtualLab import views as VirtualLabViews
from examCell import views as examCellViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',VirtualLabViews.home),
    path('',VirtualLabViews.index),
    path('teacherDasboard/',VirtualLabViews.teacherDasboard,name='teacherDasboard'),
    path('post/',VirtualLabViews.dashboard),
    path('about/',VirtualLabViews.about,name='about'),
    path('addpost/',VirtualLabViews.addpost,name='post'),
    path('coderoom/<int:id>/',VirtualLabViews.coderoom,name='coderoom'),
    path('teacher_coderoom/<int:id>/',VirtualLabViews.teacher_coderoom,name='teacher_coderoom'),
    path('runcode/<int:id>/',VirtualLabViews.run_code,name='runcode'),
    path('deletepost/<int:id>/', VirtualLabViews.deletepost, name='deletepost'),
    path('response/<int:id>/', VirtualLabViews.response, name='response'),
    path('winnerAdd/<int:id>/',VirtualLabViews.winnerAdd,name='winnerAdd'),
    path('winnerdelete/<int:id>/', VirtualLabViews.winnerDelete, name='winnerdelete'),
    path('login/',VirtualLabViews.user_login,name='userlogin'),
    path('signup/',VirtualLabViews.uesr_signup,name='usersignup'),
    path('logout/', VirtualLabViews.user_logout, name='userlogout'),
    path('winnersave/',VirtualLabViews.winnersave,name='winnersave'),
    path('Winnerboard/',VirtualLabViews.Winnerboard,name='Winnerboard'),
    path('ShowProfile/<str:name>/',VirtualLabViews.ShowProfile,name='ShowProfile'),
    path('profile/<str:name>/',VirtualLabViews.profile,name='profile'),
    path('addTest/<int:id>/',VirtualLabViews.addTest,name='addTest'),
    path('testCase/<int:id>/',VirtualLabViews.testCase,name='testCase'),
    
    path('exam/',examCellViews.examInterface, name='examInterface'),
    path('StartExam/<int:id>/',examCellViews.StartExam, name='StartExam'),
    path('showResult/<int:id>/',examCellViews.showResult, name='showResult'),
    path('examSet/',examCellViews.examEntry, name='examEntry'),
    path('EntryNewQuestion/',examCellViews.newQuestionEntry, name='newQuestionEntry'),
    path('DeleteQuestion/<int:id>/',examCellViews.DeleteQuestion, name='DeleteQuestion'),
    path('QuestionEntry/<int:id>/',examCellViews.QuestionEntry, name='QuestionEntry'),
    path('saveQuestion/<int:id>/',examCellViews.saveQuestion, name='saveQuestion'),
    path('showResultData/<int:id>/',examCellViews.showResultData, name='showResultData'),
    path('generate_excel/<int:id>/', examCellViews.generate_excel, name='generate_excel'),
]
