from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,logout as auth_logout, login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import time
# from home.views import home

def login(request):

    if request.method == "POST":

        user_login = request.POST.get('login')

        user_password = request.POST.get('password')

        user = authenticate(username=user_login, password = user_password)

        if user is not None:
            auth_login(request, user)
            # return render(request, 'ok_post.html')
            # return redirect('testinho')
            return redirect('home')
        else:
            print('esse usuário não existe!')
            messages.info(request, 'Usuário/Senha inválida', extra_tags='warning')
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')


def logout(request):
    auth_logout(request)
    return render(request, 'login.html')
    