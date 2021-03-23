from django.urls import path
from . import views


urlpatterns = [
    # esse name ='home' é o nome do endpoint
    path('', views.home, name='home'),
    path('tabela', views.info_tabela, name='tabela'),
    path('noticias', views.info_noticias, name='noticias'),
    path('galeria', views.info_galeria, name='galeria'),
    path('sobre', views.info_sobre, name='sobre')
]