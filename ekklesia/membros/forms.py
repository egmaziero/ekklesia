from django.forms import ModelForm
from .models import Pessoa, Congregacao


class PessoaForm(ModelForm):
    class Meta:
        model = Pessoa
        fields = '__all__'


class CongregacaoForm(ModelForm):
    class Meta:
        model = Congregacao
        fields = '__all__'
