from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('list_feirantes', views.list_feirantes, name='list_feirantes'),
    path('informacoes', views.informacoes, name='informacoes'),
    path('contatos', views.contatos, name='contatos'),
]