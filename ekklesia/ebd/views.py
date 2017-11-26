# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

from .forms import ClasseEBDForm, PessoaClasseEBDForm


def cadastro_classe_ebd(request):
    if request.method == "POST":
        form = ClasseEBDForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('form_saved')
    else:
        form = ClasseEBDForm()
        return render(request, 'ebd/cadastro_classe_ebd.html', {'form': form})


def cadastro_pessoa_classe_ebd(request):
    if request.method == "POST":
        form = PessoaClasseEBDForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('form_saved')
    else:
        form = PessoaClasseEBDForm()
        return render(request, 'ebd/cadastro_pessoa_classe_ebd.html', {'form': form})
