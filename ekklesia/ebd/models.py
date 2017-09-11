# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ekklesia.membros import Congregacao, Pessoa


class ClasseEBD(models.Model):
    nome = models.CharField(max_length=100)
    Congregacao = models.ForeignKey(Congregacao, on_delete=models.CASCADE)
    idadeInicio = models.IntegerField()
    idedaFim = models.IntegerField()


class PessoaClasseEBD(models.Model):
    Pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    ClasseEBD = models.ForeignKey(ClasseEBD, on_delete=models.CASCADE)
    dataInicio = models.DateField()
    dataFim = models.DateField()


class EventoEBD(models.Model):
    Congregacao = models.ForeignKey(Congregacao, on_delete=models.CASCADE)
    dataEvento = models.DateField()
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=256)


class RegistroEventoEBD(models.Model):
    EventoEBD = models.ForeignKey(EventoEBD, on_delete=models.CASCADE)
    Pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    horarioChegada = models.TimeField()
