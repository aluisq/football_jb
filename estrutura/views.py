from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,logout as auth_logout, login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import time

@login_required
def equipe(request):
    pass
