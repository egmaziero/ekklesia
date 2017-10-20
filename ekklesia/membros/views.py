# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.forms import modelformset_factory
from django.shortcuts import render
from membros.models import Pessoa

def manage_pessoa(request):
    PessoaFormSet = modelformset_factory(Pessoa, fields=('nome', 'foto'))
    if request.method == 'POST':
        formset = PessoaFormSet(request.POST, request.FILES)
        if formset.is_valid():
            formset.save()
            # do something.
    else:
        formset = PessoaFormSet()
    return render(request, 'manage_pessoa.html', {'formset': formset})