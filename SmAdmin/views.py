from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def Base(request):
    context = {}
    return render(request, 'backend/dashbord/dashbord.html', context)


@login_required(login_url='/admin/login')  # Check login
def Home(request):
    context = {}
    return render(request, 'backend/dashbord/dashbord.html', context)


def Login(request):
    if request.method == 'GET':
        context = ''
        if request.user.is_authenticated:
            return HttpResponseRedirect('/admin/')
        else:
            return render(request, 'backend/auth/login.html', {'context': context})


def DoLogin(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect('/admin/')
    else:
        context = {'error': 'Wrong credintials'}
        return HttpResponseRedirect('/admin/login')


def DoLogout(request):
    logout(request)
    return HttpResponseRedirect('/admin/')
