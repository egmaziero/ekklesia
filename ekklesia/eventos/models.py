# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import membros
from django.db import models


class EventoCargo(models.Model):
    Congregacao = models.ForeignKey(membros.models.Congregacao, on_delete=models.CASCADE)
    dataEvento = models.DateField()
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=256)


class RegistroEventoCargo(models.Model):
    EventoCargo = models.ForeignKey(EventoCargo, on_delete=models.CASCADE)
    Pessoa = models.ForeignKey(membros.models.Pessoa, on_delete=models.CASCADE)
    horarioChegada = models.TimeField()


class EventoDepartamento(models.Model):
    Congregacao = models.ForeignKey(membros.models.Congregacao, on_delete=models.CASCADE)
    dataEvento = models.DateField()
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=256)


class RegistroEventoDepartamento(models.Model):
    EventoDepartamento = models.ForeignKey(EventoDepartamento, on_delete=models.CASCADE)
    Pessoa = models.ForeignKey(membros.models.Pessoa, on_delete=models.CASCADE)
    horarioChegada = models.TimeField()


class EventoGeral(models.Model):
    Congregacao = models.ForeignKey(membros.models.Congregacao, on_delete=models.CASCADE)
    dataEvento = models.DateField()
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=256)


class RegistroEventoGeral(models.Model):
    EventoGeral = models.ForeignKey(EventoGeral, on_delete=models.CASCADE)
    Pessoa = models.ForeignKey(membros.models.Pessoa, on_delete=models.CASCADE)
    horarioChegada = models.TimeField()

