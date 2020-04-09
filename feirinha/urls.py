from django.urls import path
from . import views

urlpatterns = [
    #path('home', views.home, name='home'),
    path('', views.list_feirantes, name='list_feirantes'),
    path('informacoes', views.informacoes, name='informacoes'),
    path('contatos', views.contatos, name='contatos'),
]
