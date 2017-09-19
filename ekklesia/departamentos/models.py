# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import membros
from django.db import models


class Departamento(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=156)
    Congregacao = models.ForeignKey(membros.models.Congregacao, on_delete=models.CASCADE)


class PessoaDepartamento(models.Model):
    Pessoa = models.ForeignKey(membros.models.Pessoa, on_delete=models.CASCADE)
    Departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    dataInicio = models.DateField()
    dataFim = models.DateField()
