from django.urls import path
from . import views

urlpatterns = [
    # esse name ='home' é o nome do endpoint
    path('', views.jogador, name='jogador'),
]