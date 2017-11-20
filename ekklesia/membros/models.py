# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Pessoa(models.Model):
    # common personal information
    nome = models.CharField(max_length=100)
    foto = models.ImageField()
    dataNascimento = models.DateField()
    rg = models.CharField(max_length=20)
    cpf = models.CharField(max_length=20)
    # address
    logradouro = models.CharField(max_length=100)
    numero = models.CharField(max_length=10)
    complemento = models.CharField(max_length=50)
    bairro = models.CharField(max_length=50)
    cidade = models.CharField(max_length=70)
    estado = models.CharField(max_length=30)
    # contact
    telefone = models.CharField(max_length=20)
    celular = models.CharField(max_length=20)
    email = models.EmailField()
    dataCadastro = models.DateField()

    def __str__(self):
        return self.nome


class Congregacao(models.Model):
    nome = models.CharField(max_length=50)
    # address
    logradouro = models.CharField(max_length=100)
    numero = models.CharField(max_length=10)
    complemento = models.CharField(max_length=50)
    bairro = models.CharField(max_length=50)
    cidade = models.CharField(max_length=70)
    estado = models.CharField(max_length=30)
    # contact
    telefone = models.CharField(max_length=20)
    celular = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.nome


class PessoaCongregacao(models.Model):
    Pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    Congregacao = models.ForeignKey(Congregacao, on_delete=models.CASCADE)


class Cargo(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=156)

    def __str__(self):
        return self.nome


class PessoaCargo(models.Model):
    Pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    Cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE)
    dataInicio = models.DateField()
    dataFim = models.DateField()


class Funcao(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=156)

    def __str__(self):
        return self.nome


class PessoaFuncao(models.Model):
    Pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    Funcao = models.ForeignKey(Funcao, on_delete=models.CASCADE)
    dataInicio = models.DateField()
    dataFim = models.DateField()
