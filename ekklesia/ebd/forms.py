from django.forms import ModelForm
from .models import ClasseEBD, PessoaClasseEBD


class ClasseEBDForm(ModelForm):
    class Meta:
        model = ClasseEBD
        fields = '__all__'


class PessoaClasseEBDForm(ModelForm):
    class Meta:
        model = PessoaClasseEBD
        fields = '__all__'
