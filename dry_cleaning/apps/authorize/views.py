from django.contrib.auth import authenticate, login, logout, get_user_model
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.models import User
from .models import *
from django.http import HttpResponseRedirect


def index(request):
    return render(request, 'base.html')


def log_out(request):
    logout(request)
    return HttpResponseRedirect(reverse('authorize:index'))


def reg(request):
    UserModel = get_user_model()
    user = UserModel.objects.create_user(username=request.POST['username'],
                                         password=request.POST['password'])
    user.save()
    profile = Profile.objects.create(user=user,
                                     position=request.POST['position'],
                                         phone=request.POST['phone'],
                                     total=0)
    profile.save()
    return HttpResponseRedirect(reverse('authorize:signin'))


def log(request):
    user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
    if user is not None:
        login(request, user)
        print('Вход осуществлён')
        return HttpResponseRedirect(reverse('authorize:index'))
    else:
        print(user)
        print('Не получилось войти')
        return HttpResponseRedirect(reverse('authorize:signin'))


def getusers(request):
    a = User.objects.all()
    return render(request, 'registration/users.html', {'users': a})


def signup(request):
    return render(request, 'signup.html')


def signin(request):
    return render(request, 'authorize/login.html')
