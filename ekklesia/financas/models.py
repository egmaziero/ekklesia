# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import membros
import departamentos

class EntradaFinanceira(models.Model):
    Departamento = models.ForeignKey(departamentos.models.Departamento, on_delete=models.CASCADE)
    Pessoa = models.ForeignKey(membros.models.Pessoa, on_delete=models.CASCADE, related_name='giver')
    valor = models.FloatField()
    mesReferencia = models.IntegerField()
    dataEntrada = models.DateField()
    responsavel = models.ForeignKey(membros.models.Pessoa, on_delete=models.CASCADE, related_name='receiver')
