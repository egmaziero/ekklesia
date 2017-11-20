from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^cadastroPessoa/$', views.cadastro_pessoa, name='cadastro_pessoa'),
    url(r'^cadastroCongregacao/$', views.cadastro_congregacao, name='cadastro_congregacao'),
]
