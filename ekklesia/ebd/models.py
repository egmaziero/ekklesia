# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import membros
from django.db import models


class ClasseEBD(models.Model):
    nome = models.CharField(max_length=100)
    Congregacao = models.ForeignKey(membros.models.Congregacao, on_delete=models.CASCADE)
    idadeInicio = models.IntegerField()
    idedaFim = models.IntegerField()

    def __str__(self):
        return self.nome


class PessoaClasseEBD(models.Model):
    Pessoa = models.ForeignKey(membros.models.Pessoa, on_delete=models.CASCADE)
    ClasseEBD = models.ForeignKey(ClasseEBD, on_delete=models.CASCADE)
    dataInicio = models.DateField()
    dataFim = models.DateField()

    def __str__(self):
        return self.nome


class EventoEBD(models.Model):
    Congregacao = models.ForeignKey(membros.models.Congregacao, on_delete=models.CASCADE)
    dataEvento = models.DateField()
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=256)

    def __str__(self):
        return self.nome


class RegistroEventoEBD(models.Model):
    EventoEBD = models.ForeignKey(EventoEBD, on_delete=models.CASCADE)
    Pessoa = models.ForeignKey(membros.models.Pessoa, on_delete=models.CASCADE)
    horarioChegada = models.TimeField()

    def __str__(self):
        return self.nome
