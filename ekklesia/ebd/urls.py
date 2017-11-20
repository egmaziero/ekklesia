from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^cadastroClasseEBD/$', views.cadastro_classe_ebd, name='cadastro_classe_ebd'),
    url(r'^ebd:cadastroPessoaClasseEBD/$', views.cadastro_pessoa_classe_ebd, name='cadastro_pessoa_classe_ebd'),
]
