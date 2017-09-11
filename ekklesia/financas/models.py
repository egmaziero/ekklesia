# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ekklesia.membros import Pessoa
from ekklesia.departamentos import Departamento

class EntradaFinanceira(models.Model):
    Departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    Pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    valor = models.FloatField()
    mesReferencia = models.IntegerField()
    dataEntrada = models.DateField()
    responsavel = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
