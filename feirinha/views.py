from django.shortcuts import render
from .models import Feirante, Produto


def home(request):
	feirantes = Feirante.objects.all() 
	produtos = Produto.objects.all()
	return render(request, 'feirinha/index.html',
					{'feirantes': feirantes, 'produtos': produtos})

def informacoes():
	pass	

def contatos():
	pass


def list_feirantes(request):
	feirantes = Feirante.objects.all() 
	produtos = Produto.objects.all()
	return render(request, 'feirinha/list_feirantes.html', {'feirantes': feirantes, 'produtos': produtos})