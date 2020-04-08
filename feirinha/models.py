from django.db import models
from django.conf import settings
from django.utils import timezone
from django.core.validators import MinValueValidator


class Feirante(models.Model):
	nome = models.CharField(verbose_name='nome',max_length=200)
	horario_funcionamento = models.CharField(max_length=50)
	taxa_entrega = models.DecimalField(verbose_name='taxa de entrega',
                               		   decimal_places=2,
                                	   max_digits=14,
                                       validators=[MinValueValidator(0.00)])
	telefone = models.CharField(verbose_name='telefone', max_length=20)
	
	#retonar o nome do feirante
	def __str__(self):
		return self.nome


class Unidade(models.Model):
	# Tipos de unidades
	# Adicionar alguma que eu esteja esquecendo
	MACO = 'M'
	PACOTE = 'P'
	QUILO = 'Q'
	UNIDADE = 'U'
	DUZIA = 'D'

	TIPOS = ((MACO, 'Maço'),
			 (PACOTE, 'Pacote'),
			 (QUILO, 'Quilo'),
			 (UNIDADE, 'Unidade'),
			 (DUZIA, 'Dúzia'),)

	tipo = models.CharField(verbose_name='nome', max_length=1, choices=TIPOS)

	#retonar o tipo da unidade de venda(ex. preço, maço, pacote, quilo)
	def __str__(self):
		return self.tipo


class Produto(models.Model):
	feirante = models.ForeignKey(Feirante, 
								 models.CASCADE,
								 related_name='feirante')
	nome = models.CharField(verbose_name='nome', max_length=200)
	valor = models.DecimalField(verbose_name='valor',
                                decimal_places=2,
                                max_digits=14,
                                validators=[MinValueValidator(0.00)])
	unidade = models.ForeignKey(Unidade, models.CASCADE,related_name='unidade')
	foto = models.ImageField(verbose_name='Foto', null=True, blank=True)
	quantidade = models.PositiveIntegerField(verbose_name='quantidade', default=0)

	#retonar o nome do produto	
	def __str__(self):
		nome_produto = self.nome +' - '+ self.feirante.nome 
		return nome_produto
