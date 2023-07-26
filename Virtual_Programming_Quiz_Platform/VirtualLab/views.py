from django.shortcuts import render, HttpResponseRedirect, HttpResponse
import datetime
import os
from subprocess import Popen, PIPE
from django.contrib import messages
from django.utils import timezone
from .models import codePost
from .models import userVisitData
from .models import sub_code
from .models import winnerSave
from .models import testCases
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User

# for index page for users


def index(request):
    return render(request, 'home.html')


def home(request):
    postData = codePost.objects.all().order_by('post_dat').reverse()
    if request.user.is_authenticated:
        if request.user.is_staff == True:
            return render(request, 'index_teacher.html', {'postData': postData})
    return render(request, 'index.html', {'postData': postData})


#   index page for teacher

def teacherDasboard(request):
    postData = codePost.objects.all().order_by('post_dat').reverse()
    return render(request, 'index_teacher.html', {'postData': postData})

#  for create post page


def dashboard(request):
    if (request.user.is_authenticated and request.user.is_staff) == True:
        return render(request, 'post.html')
    else:
        return HttpResponseRedirect('/home/')

# for about page


def about(request):
    return render(request, 'about.html')

#  for when post data submit


def addpost(request):
    if (request.user.is_authenticated and request.user.is_staff) == True:
        if request.method == 'GET':
            titel = request.GET['code_title']
            codeEXP = request.GET['code_exp']
            inp = request.GET['sample_inp']
            out = request.GET['sample_out']
            stTime = datetime.datetime.now().strftime("%Y-%m-%d,%H:%M")
            Date = request.GET.get('date', '')
            Time = request.GET.get('time', '')
            endTime = Date + ',' + Time
            save_data = codePost(title=titel, post_dat=stTime, end_Data=endTime,
                                 code_exp=codeEXP, codeinput=inp, codeoutput=out)
            save_data.save()

            return HttpResponseRedirect('/home/')
    else:
        return HttpResponseRedirect('/login/')
#  when click on code enter code room


def coderoom(request, id):
    if request.user.is_authenticated:
        userName = request.user.username
        time = datetime.datetime.now()
        if userVisitData.objects.filter(usename=userName).exists():
            VisitInformation = userVisitData.objects.get(usename=userName)
            VisitInformation.codeId = id
            VisitInformation.stTime = time
        else:
            VisitInformation = userVisitData(
                codeId=id, stTime=time, usename=userName)
        VisitInformation.save()
        postData = codePost.objects.get(pk=id)
        return render(request, 'coderoom.html', {'postData': postData, 'value': ''})
    else:
        return HttpResponseRedirect('/login/')


# coderoom for teacher


def teacher_coderoom(request, id):
    postData = codePost.objects.get(pk=id)
    return render(request, 'Teacher_coderoom.html', {'postData': postData})

# for responce Panel


def response(request, id):
    if request.user.is_authenticated and request.user.is_staff:
        codeTitle = codePost.objects.get(id=id)
        title = codeTitle.title
        responce_code = sub_code.objects.filter(codeTitel=title)
        return render(request, 'responce_panle.html', {'response': responce_code, 'codeData': codeTitle})

# for Winner add Panel


def winnerAdd(request, id):
    if request.user.is_authenticated and request.user.is_staff:
        codeData = codePost.objects.get(pk=id)
        Title = codeData.title
        win = winnerSave.objects.filter(Title=codeData.title)
        if winnerSave.objects.filter(Title=codeData.title).exists():
            return render(request, 'WinnerAdd.html', {'codeData': Title, 'winner': win})
        return render(request,  'WinnerAdd.html', {'codeData': Title, 'winner': win})
    else:
        return HttpResponseRedirect('/home/')

# for save winner data

def winnersave(request):
    if request.method == 'POST':
        uname = request.POST['winnerUser']
        title = request.POST['codeTitel']
        time = request.POST['time']
        data = winnerSave(username=uname, Title=title, Sub_time=time)
        data.save()
        return HttpResponseRedirect('/home/')

# for delete winner data
def winnerDelete(request,id):
    if winnerSave.objects.filter(pk=id).exists():
        codeData = winnerSave.objects.get(pk=id)
        Title = codeData.Title
        test = codePost.objects.get(title=Title)
        codeData.delete()
        Title2 = test.title
        win = winnerSave.objects.filter(Title=codeData.Title)
        return render(request,  'WinnerAdd.html', {'codeData': Title2, 'winner': win})
    return HttpResponseRedirect('/home/')
# for login


def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                if user.is_staff == True:
                    login(request, user)
                    return HttpResponseRedirect('/teacherDasboard/')
                else:
                    login(request, user)
                    return HttpResponseRedirect('/home/')
            else:
                messages.success(
                    request, "Password Not match. Re-enter password correctly.")
                return HttpResponseRedirect('/login/')
        else:
            return render(request, 'login.html')
    else:
        return HttpResponseRedirect('/home/')


def uesr_signup(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        user = request.POST['uname']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        email = request.POST['email']
        if(pass1 == pass2):
            user_exist = User.objects.filter(username=user).exists()
            if user_exist:
                messages.success(
                    request, 'This username already exists. Please use a different one.')
                return HttpResponseRedirect("/signup/")
            else:
                myuser = User.objects.create_user(user, email, pass1)
                myuser.first_name = fname
                myuser.last_name = lname
                myuser.save()

                # for login after signup
                user = authenticate(request, username=user, password=pass1)
                if user is not None:
                    login(request, user)
                    return HttpResponseRedirect('/home/')

        else:
            messages.success(
                request, "Password Not match. Re-enter password correctly.")
            return HttpResponseRedirect("/signup/")
    else:
        return render(request, 'sign_up.html')

# for user logout


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/home/')

# for delete Post


def deletepost(request, id):
    if request.user.is_authenticated and request.user.is_staff:
        postCode = codePost.objects.get(pk=id)
        win = winnerSave.objects.filter(Title=postCode.title)
        win.delete()
        postCode.delete()
        return HttpResponseRedirect('/teacherDasboard/')
    else:
        return HttpResponseRedirect('/login/')


# for winner Board
def Winnerboard(request):
    if request.user.is_authenticated:
        winnerDatas = winnerSave.objects.all().order_by('id').reverse()
        return render(request, 'WinnerBoard.html', {'winner': winnerDatas})
    else:
        return HttpResponseRedirect('/login/')


def ShowProfile(request, name):
    if request.user.is_authenticated:
        userdata = User.objects.get(username=name)
        return render(request, "profile.html", {'name': userdata})
    else:
        return HttpResponseRedirect('/login/')


def profile(request, name):
    if request.user.is_authenticated:
        userdata = User.objects.get(username=name)
        return render(request, "profile.html", {'name': userdata})
    else:
        return HttpResponseRedirect('/login/')


def testCase(request, id):
    postData = codePost.objects.get(pk=id)
    if testCases.objects.filter(codeId=id).exists() == False:
        return render(request, 'testCase.html', {'PostId': id, 'postData': postData})
    messages.success(request, 'Already Present testCase for this code')
    returnObj = str(id)
    return HttpResponseRedirect('/teacher_coderoom/'+returnObj)

# test case add


def addTest(request, id):
    postData = codePost.objects.get(pk=id)
    if request.method == 'POST':
        codeId = id
        testInp = request.POST['testInp']
        testOut = request.POST['testOut']
        if testInp != '' and testOut != '':
            data = testCases(codeId=codeId, testInp=testInp, testOut=testOut)
            data.save()
            messages.success(request, 'Successfully add test case')
        else:
            messages.error(request, 'Please re-enter test Input and Output')
        returnid = str(id)
        return render(request, 'testCase.html', {'PostId': returnid, 'postData': postData})

# --------------------------------------------------------------------------------------------------------------------
# for compiler


def run_code(request, id):
    if 'run' in request.POST:
        code_input = ''
        data = request.POST['codes']
        code = request.POST.get('codebox', '')

        #   -------------------------  -----------------------------------------
        # for Python
        if data == 'Python':
            code_input = request.POST.get('output', '')
            if code:
                python_dir = os.path.join(os.getcwd(), 'python')
                os.makedirs(python_dir, exist_ok=True)

                python_file_path = os.path.join(python_dir, 'test.py')
                try:
                    with open(python_file_path, 'w') as f:
                        f.write(code)
                except IOError:
                    return HttpResponse('Error: Could not write to file.')
            cmd = ['python', 'python/test.py']
            process = Popen(cmd, stdout=PIPE, stdin=PIPE, stderr=PIPE)
            output, error = process.communicate(input=code_input.encode())
            output = output.decode('utf-8')
            error = error.decode('utf-8')
            if output:
                messages.success(request, '\n'+output)
            else:
                messages.success(request, '\n'+error)

        #   --------------------------  -------------------------------------

        # for Javas

        elif data == 'Java':
            code_input = request.POST.get('output', '')

            if code:
                java_dir = os.path.join(os.getcwd(), 'java')
                os.makedirs(java_dir, exist_ok=True)

                java_file_path = os.path.join(java_dir, 'Main.java')
                try:
                    with open(java_file_path, 'w') as f:
                        f.write(code)
                except IOError:
                    return HttpResponse('Error: Could not write to file.')

            # cmd = ['java', 'java/Main.java']
            # try:
            #     process = Popen(cmd, stdout=PIPE, stdin=PIPE, stderr=PIPE)
            #     output, error = process.communicate(input=code_input.encode())
            #     output = output.decode('utf-8')
            #     error = error.decode('utf-8')
            #     if output:
            #         messages.success(request, '\n'+output)
            #     else:
            #         messages.success(request, '\n'+error)
            # except Exception as e:
            #     print("Exception:", str(e))
            compile_cmd = ['javac', 'Main.java']
            compile_process = Popen(
                compile_cmd, cwd=java_dir, stdout=PIPE, stderr=PIPE)
            compile_output, compile_errors = compile_process.communicate(
                input=code_input.encode())

            if compile_process.returncode == 0:
                execute_cmd = ['java', 'Main']
                execute_process = Popen(
                    execute_cmd, cwd=java_dir, stdout=PIPE, stdin=PIPE, stderr=PIPE)
                execute_output, execute_errors = execute_process.communicate(
                    input=code_input.encode(), timeout=5)

                if execute_output:
                    messages.success(
                        request, '\n'+execute_output.decode('utf-8'))
                else:
                    messages.success(
                        request, '\n'+execute_errors.decode('utf-8'))

            else:
                messages.success(request, '\n'+compile_errors.decode('utf-8'))

        #   -----------------------------   ---------------------------------------
 # for C / C++

        elif data == 'Cpp':
            code_input = request.POST.get('output', '')
            cpp_dir = '/tmp/cpp'  # Use a temporary directory instead of 'cpp'
            os.makedirs(cpp_dir, exist_ok=True)

            cpp_file_path = os.path.join(cpp_dir, 'my_cpp_code.cpp')
            try:
                with open(cpp_file_path, 'w') as f:
                    f.write(code)
            except IOError:
                return HttpResponse('Error: Could not write to file.')

            compile_cmd = ['g++', '-o', 'my_cpp_code', 'my_cpp_code.cpp']
            compile_process = Popen(
                compile_cmd, cwd=cpp_dir, stdout=PIPE, stderr=PIPE)
            compile_output, compile_errors = compile_process.communicate(
                input=code_input.encode())

            if compile_process.returncode == 0:
                # Remove the 'cpp' directory from the path
                execute_cmd = ['./my_cpp_code']
                execute_process = Popen(
                    execute_cmd, cwd=cpp_dir, stdout=PIPE, stdin=PIPE, stderr=PIPE)
                execute_output, execute_errors = execute_process.communicate(
                    input=code_input.encode(), timeout=5)

                if execute_output:
                    messages.success(
                        request, '\n'+execute_output.decode('utf-8'))
                else:
                    messages.success(
                        request, '\n'+execute_errors.decode('utf-8'))

            else:
                messages.success(request, '\n'+compile_errors.decode('utf-8'))

        # workspace = {}
        postData = codePost.objects.get(pk=id)
        return render(request, 'coderoom.html', {'postData': postData, 'value': code})

    if 'sub' in request.POST:

        if testCases.objects.filter(codeId=id).exists():

            # this code for all ans accept

            testcase = testCases.objects.filter(codeId=id).first()
            code_input = testcase.testInp.lower()
            if code_input == 'null':
                userName = request.user.username
                endTime = datetime.datetime.now()
                data = userVisitData.objects.get(codeId=id, usename=userName)
                codeTitle = codePost.objects.get(id=id)
                title = codeTitle.title
                aware_datetime = timezone.make_aware(
                    endTime, timezone.get_default_timezone())
                processTime = (aware_datetime-data.stTime).total_seconds()
                lang = request.POST['codes']
                code = request.POST.get('codebox', '')
                save_data = sub_code(
                    user=userName, sub_time=processTime, codeTitel=title, sub_lang=lang, sub_data=code)
                save_data.save()
                return HttpResponseRedirect('/home/')

            # for testcase run
            dataFT = testCases.objects.filter(codeId=id).first()
            dataLT = testCases.objects.filter(codeId=id).last()
            r1 = int(dataFT.id)
            r2 = int(dataLT.id)
            output = ''
            checking = 0
            for i in range(r1, r2+1):
                testcase = testCases.objects.get(id=i)
                code_input = testcase.testInp
                data = request.POST['codes']
                code = request.POST.get('codebox', '')

                # for Python
                if data == 'Python':
                    if code:
                        python_dir = os.path.join(os.getcwd(), 'python')
                        os.makedirs(python_dir, exist_ok=True)

                        python_file_path = os.path.join(python_dir, 'test.py')
                        try:
                            with open(python_file_path, 'w') as f:
                                f.write(code)
                        except IOError:
                            return HttpResponse('Error: Could not write to file.')
                    cmd = ['python', 'python/test.py']
                    process = Popen(cmd, stdout=PIPE, stdin=PIPE, stderr=PIPE)
                    output, error = process.communicate(
                        input=code_input.encode())
                    output = output.decode('utf-8')
                    error = error.decode('utf-8')

                # for Javas

                elif data == 'Java':

                    if code:
                        java_dir = os.path.join(os.getcwd(), 'java')
                        os.makedirs(java_dir, exist_ok=True)

                        java_file_path = os.path.join(java_dir, 'Main.java')
                        try:
                            with open(java_file_path, 'w') as f:
                                f.write(code)
                        except IOError:
                            return HttpResponse('Error: Could not write to file.')

                    # cmd = ['java', 'java/Main.java']
                    # try:
                    #     process = Popen(cmd, stdout=PIPE, stdin=PIPE, stderr=PIPE)
                    #     output, error = process.communicate(input=code_input.encode())
                    #     output = output.decode('utf-8')
                    #     error = error.decode('utf-8')

                    # except Exception as e:
                    #         print("Exception:", str(e))
                    compile_cmd = ['javac', 'Main.java']
                    compile_process = Popen(
                        compile_cmd, cwd=java_dir, stdout=PIPE, stderr=PIPE)
                    compile_output, compile_errors = compile_process.communicate(
                        input=code_input.encode())

                    if compile_process.returncode == 0:
                        execute_cmd = ['java', 'Main']
                        execute_process = Popen(
                            execute_cmd, cwd=java_dir, stdout=PIPE, stdin=PIPE, stderr=PIPE)
                        execute_output, execute_errors = execute_process.communicate(
                            input=code_input.encode(), timeout=5)
                        output = execute_output.decode('utf-8')
                        error = execute_errors.decode('utf-8')

                # for C / C++

                elif data == 'Cpp':
                    cpp_dir = os.path.join(os.getcwd(), 'cpp')
                    os.makedirs(cpp_dir, exist_ok=True)

                    cpp_file_path = os.path.join(cpp_dir, 'my_cpp_code.cpp')
                    try:
                        with open(cpp_file_path, 'w') as f:
                            f.write(code)
                    except IOError:
                        return HttpResponse('Error: Could not write to file.')

                    compile_cmd = ['g++', '-o',
                                   'my_cpp_code', 'my_cpp_code.cpp']
                    compile_process = Popen(
                        compile_cmd, cwd=cpp_dir, stdout=PIPE, stderr=PIPE)
                    compile_output, compile_errors = compile_process.communicate(
                        input=code_input.encode())

                    if compile_process.returncode == 0:
                        execute_cmd = ['./cpp/my_cpp_code']
                        execute_process = Popen(
                            execute_cmd, cwd=cpp_dir, stdout=PIPE, stdin=PIPE, stderr=PIPE)
                        execute_output, execute_errors = execute_process.communicate(
                            input=code_input.encode(), timeout=5)
                        output = execute_output.decode('utf-8')

                #  test case checking

                output = str(output.strip())
                code_out = str(testcase.testOut.strip())
                if output == code_out:
                    print('Pass Case ', end='')
                    print(i)
                    checking += 1
                else:
                    print('Not Pass Case ', end='')
                    print(i)

                i += 1

            if checking == (r2-r1)+1:
                userName = request.user.username
                endTime = datetime.datetime.now()
                data = userVisitData.objects.get(codeId=id, usename=userName)
                codeTitle = codePost.objects.get(id=id)
                title = codeTitle.title
                aware_datetime = timezone.make_aware(
                    endTime, timezone.get_default_timezone())
                processTime = (aware_datetime-data.stTime).total_seconds()
                lang = request.POST['codes']
                code = request.POST.get('codebox', '')
                save_data = sub_code(
                    user=userName, sub_time=processTime, codeTitel=title, sub_lang=lang, sub_data=code)
                save_data.save()
                return HttpResponseRedirect('/home/')
            else:
                messages.success(request, '\nAll Test Case not Pass')

        else:
            userName = request.user.username
            endTime = datetime.datetime.now()
            data = userVisitData.objects.get(codeId=id, usename=userName)
            codeTitle = codePost.objects.get(id=id)
            title = codeTitle.title
            aware_datetime = timezone.make_aware(
                endTime, timezone.get_default_timezone())
            processTime = (aware_datetime-data.stTime).total_seconds()
            lang = request.POST['codes']
            code = request.POST.get('codebox', '')
            save_data = sub_code(user=userName, sub_time=processTime,
                                 codeTitel=title, sub_lang=lang, sub_data=code)
            save_data.save()
            return HttpResponseRedirect('/home/')
        postData = codePost.objects.get(pk=id)
        return render(request, 'coderoom.html', {'postData': postData, 'value': code})
