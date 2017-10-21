from django.forms import ModelForm
from membros.models import Pessoa

class PessoaForm(ModelForm):
    class Meta:
        model = Pessoa

form = PessoaForm()