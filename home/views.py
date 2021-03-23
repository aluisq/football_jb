from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
import time

@login_required
def home(request):
    return render(request, 'home.html')

@login_required
def info_tabela(request):
    return render(request, 'tabela.html')

@login_required
def info_noticias(request):
    return render(request, 'noticias.html')
    
@login_required
def info_sobre(request):
    return render(request, 'sobre.html')


@login_required
def info_galeria(request):
    return render(request, 'galeria.html')