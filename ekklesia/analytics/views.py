from django.http import HttpResponse
from django.template import loader

from membros.models import Pessoa


def index(request):
    pessoas_list = Pessoa.objects.order_by('dataCadastro')[:20]
    template = loader.get_template('analytics/index.html')
    context = {
        'pessoas_list': pessoas_list,
    }
    return HttpResponse(template.render(context, request))