# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-18 12:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('membros', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClasseEBD',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('idadeInicio', models.IntegerField()),
                ('idedaFim', models.IntegerField()),
                ('Congregacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='membros.Congregacao')),
            ],
        ),
        migrations.CreateModel(
            name='EventoEBD',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataEvento', models.DateField()),
                ('nome', models.CharField(max_length=50)),
                ('descricao', models.CharField(max_length=256)),
                ('Congregacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='membros.Congregacao')),
            ],
        ),
        migrations.CreateModel(
            name='PessoaClasseEBD',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataInicio', models.DateField()),
                ('dataFim', models.DateField()),
                ('ClasseEBD', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ebd.ClasseEBD')),
                ('Pessoa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='membros.Pessoa')),
            ],
        ),
        migrations.CreateModel(
            name='RegistroEventoEBD',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('horarioChegada', models.TimeField()),
                ('EventoEBD', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ebd.EventoEBD')),
                ('Pessoa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='membros.Pessoa')),
            ],
        ),
    ]