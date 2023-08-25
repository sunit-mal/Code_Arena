from django.contrib import admin
from django.urls import path
from VirtualLab import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.home),
    path('',views.index),
    path('teacherDasboard/',views.teacherDasboard,name='teacherDasboard'),
    path('post/',views.dashboard),
    path('about/',views.about,name='about'),
    path('addpost/',views.addpost,name='post'),
    path('coderoom/<int:id>/',views.coderoom,name='coderoom'),
    path('teacher_coderoom/<int:id>/',views.teacher_coderoom,name='teacher_coderoom'),
    path('runcode/<int:id>/',views.run_code,name='runcode'),
    path('deletepost/<int:id>/', views.deletepost, name='deletepost'),
    path('response/<int:id>/', views.response, name='response'),
    path('winnerAdd/<int:id>/',views.winnerAdd,name='winnerAdd'),
    path('winnerdelete/<int:id>/', views.winnerDelete, name='winnerdelete'),
    path('login/',views.user_login,name='userlogin'),
    path('signup/',views.uesr_signup,name='usersignup'),
    path('logout/', views.user_logout, name='userlogout'),
    path('winnersave/',views.winnersave,name='winnersave'),
    path('Winnerboard/',views.Winnerboard,name='Winnerboard'),
    path('ShowProfile/<str:name>/',views.ShowProfile,name='ShowProfile'),
    path('profile/<str:name>/',views.profile,name='profile'),
    path('addTest/<int:id>/',views.addTest,name='addTest'),
    path('testCase/<int:id>/',views.testCase,name='testCase'),
]
