from django.db import models
from django.conf import settings
from django.utils import timezone

class Feirante(models.Model):
	nome = models.CharField(max_length=200)
	horario_funcionamento = models.CharField(max_length=200)
	taxa_entrega = models.CharField(max_length=20)
	telefone = models.CharField(max_length=200)
	
	#retonar o nome do feirante
	def __str__(self):
		return self.nome

class Unidade(models.Model):
	tipo = models.CharField(max_length=200)

	#retonar o tipo da unidade de venda(ex. preço, maço, pacote, quilo)
	def __str__(self):
		return self.tipo

class Produto(models.Model):
	feirante = models.ForeignKey(Feirante, models.CASCADE,related_name='feirante')
	nome = models.CharField(max_length=200)
	valor = models.CharField(max_length=20)
	unidade = models.ForeignKey(Unidade, models.CASCADE,related_name='unidade')

	#retonar o nome do produto	
	def __str__(self):
		nome_produto = self.nome +' - '+ self.feirante.nome 
		return nome_produto
