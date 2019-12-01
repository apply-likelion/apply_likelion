from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .forms import LoginForm, UserForm
from .models import User
# from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib import auth
from django.http import HttpResponse


#합격자 목록(모든 합격자들의 이름, 폰번호,이메일 나와야됨)
def passed (request, pass_or_not = True): 
    successfulcandidates = User.objects.filter(pass_or_not= True)
    return render(request, 'account/passlist.html',{'successfulcandidates':successfulcandidates})


#임시페이지 보여주기 나중에 삭제

def detail(request):
    return render(request,'account/detail.html')




# 나의 합격여부를 알려주는 페이지

def mystate(request, pass_or_not = True): 
    if pass_or_not == True:
        p_or_n_message = " 축하드립니다 합격입니다!"
        return render(request, 'account/acceptance.html',{'p_or_n_message':p_or_n_message})
    else:
        p_or_n_message = "다음기회에"
        return render(request, 'account/acceptance.html',{'p_or_n_message':p_or_n_message})

def layout(request):
    return render(request, 'account/layout.html')

def index(request):
    users = User.objects
    return render(request, 'account/index.html')

#로그인함수
def signin(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect('account:index')
        else:
            return HttpResponse('로그인 실패. 다시 시도 해보세요.')
    else:
        form = LoginForm()
        return render(request, 'account/signin.html', {'form':form})

#로그아웃함수
def logout(request):
    auth.logout(request)
    return render(request, 'account/layout.html')

#회원가입함수
def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(username=form.cleaned_data["username"],student_id=form.cleaned_data["student_id"],major=form.cleaned_data["major"],grade=form.cleaned_data["grade"],phone_number=form.cleaned_data["phone_number"],password=form.cleaned_data["password"])
            login(request, new_user)
            return redirect('account:index')
        else:
            return HttpResponse('사용자명이 이미 존재합니다.')
    else:
        form = UserForm()
        return render(request, 'account/signup.html', {'form':form})
