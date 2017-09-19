# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-13 13:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('descricao', models.CharField(max_length=156)),
            ],
        ),
        migrations.CreateModel(
            name='Congregacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('logradouro', models.CharField(max_length=100)),
                ('numero', models.CharField(max_length=10)),
                ('complemento', models.CharField(max_length=50)),
                ('bairro', models.CharField(max_length=50)),
                ('cidade', models.CharField(max_length=70)),
                ('estado', models.CharField(max_length=30)),
                ('telefone', models.CharField(max_length=20)),
                ('celular', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Funcao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('descricao', models.CharField(max_length=156)),
            ],
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('foto', models.ImageField(upload_to=b'')),
                ('dataNascimento', models.DateField()),
                ('rg', models.CharField(max_length=20)),
                ('cpf', models.CharField(max_length=20)),
                ('logradouro', models.CharField(max_length=100)),
                ('numero', models.CharField(max_length=10)),
                ('complemento', models.CharField(max_length=50)),
                ('bairro', models.CharField(max_length=50)),
                ('cidade', models.CharField(max_length=70)),
                ('estado', models.CharField(max_length=30)),
                ('telefone', models.CharField(max_length=20)),
                ('celular', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('dataCadastro', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='PessoaCargo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataInicio', models.DateField()),
                ('dataFim', models.DateField()),
                ('Cargo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='membros.Cargo')),
                ('Pessoa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='membros.Pessoa')),
            ],
        ),
        migrations.CreateModel(
            name='PessoaCongregacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Congregacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='membros.Congregacao')),
                ('Pessoa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='membros.Pessoa')),
            ],
        ),
        migrations.CreateModel(
            name='PessoaFuncao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataInicio', models.DateField()),
                ('dataFim', models.DateField()),
                ('Funcao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='membros.Funcao')),
                ('Pessoa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='membros.Pessoa')),
            ],
        ),
    ]