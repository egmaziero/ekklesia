from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.shortcuts import redirect

from .models import Pessoa
from .forms import PessoaForm, CongregacaoForm


def index(request):
    pessoas_list = Pessoa.objects.order_by('dataCadastro')[:20]
    template = loader.get_template('membros/index.html')
    context = {
        'pessoas_list': pessoas_list,
    }
    return HttpResponse(template.render(context, request))


def cadastro_pessoa(request):
    if request.method == "POST":
        form = PessoaForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('form_saved')
    else:
        form = PessoaForm()
        return render(request, 'membros/cadastro_pessoa.html', {'form': form})


def cadastro_congregacao(request):
    if request.method == "POST":
        form = CongregacaoForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('form_saved')
    else:
        form = CongregacaoForm()
        return render(request, 'membros/cadastro_congregacao.html', {'form': form})
