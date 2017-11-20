# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .forms import ClasseEBDForm, PessoaClasseEBDForm


def cadastro_classe_ebd(request):
    form = ClasseEBDForm()
    return render(request, 'ebd/cadastro_classe_ebd.html', {'form': form})


def cadastro_pessoa_classe_ebd(request):
    form = PessoaClasseEBDForm()
    return render(request, 'ebd/cadastro_pessoa_classe_ebd.html', {'form': form})
