# Generated by Django 3.0.5 on 2020-04-08 01:27

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feirinha', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Foto'),
        ),
        migrations.AddField(
            model_name='produto',
            name='quantidade',
            field=models.PositiveIntegerField(default=0, verbose_name='quantidade'),
        ),
        migrations.AlterField(
            model_name='feirante',
            name='horario_funcionamento',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='feirante',
            name='nome',
            field=models.CharField(max_length=200, verbose_name='nome'),
        ),
        migrations.AlterField(
            model_name='feirante',
            name='taxa_entrega',
            field=models.DecimalField(decimal_places=2, max_digits=14, validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='taxa de entrega'),
        ),
        migrations.AlterField(
            model_name='feirante',
            name='telefone',
            field=models.CharField(max_length=20, verbose_name='telefone'),
        ),
        migrations.AlterField(
            model_name='produto',
            name='nome',
            field=models.CharField(max_length=200, verbose_name='nome'),
        ),
        migrations.AlterField(
            model_name='produto',
            name='valor',
            field=models.DecimalField(decimal_places=2, max_digits=14, validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='valor'),
        ),
        migrations.AlterField(
            model_name='unidade',
            name='tipo',
            field=models.CharField(choices=[('M', 'Maço'), ('P', 'Pacote'), ('Q', 'Quilo'), ('U', 'Unidade'), ('D', 'Dúzia')], max_length=1, verbose_name='nome'),
        ),
    ]