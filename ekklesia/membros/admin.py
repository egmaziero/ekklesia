# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Pessoa, Congregacao, PessoaCongregacao, Cargo, PessoaCargo, Funcao, PessoaFuncao

admin.site.register(Pessoa)
admin.site.register(Congregacao)
admin.site.register(PessoaCongregacao)
admin.site.register(Cargo)
admin.site.register(PessoaCargo)
admin.site.register(Funcao)
admin.site.register(PessoaFuncao)
