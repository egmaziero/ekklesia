from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render


from .models import Pessoa
from .forms import PessoaForm


def index(request):
    pessoas_list = Pessoa.objects.order_by('dataCadastro')[:20]
    template = loader.get_template('membros/index.html')
    context = {
        'pessoas_list': pessoas_list,
    }
    return HttpResponse(template.render(context, request))

def cadastro_pessoa(request):
    form = PessoaForm()
    return render(request, 'membros/cadastro_pessoa.html', {'form': form})