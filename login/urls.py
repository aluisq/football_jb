from django.urls import path
from . import views


urlpatterns = [
    # esse name ='home' é o nome do endpoint
    path('', views.login, name='login'),
    path('', views.logout, name='logout'),
]