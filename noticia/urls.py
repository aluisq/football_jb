from django.urls import path
from . import views

urlpatterns = [
    path('', views.noticia, name='noticias'),
]