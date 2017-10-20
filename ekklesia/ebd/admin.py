# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import ClasseEBD, PessoaClasseEBD, EventoEBD, RegistroEventoEBD

admin.site.register(ClasseEBD)
admin.site.register(PessoaClasseEBD)
admin.site.register(EventoEBD)
admin.site.register(RegistroEventoEBD)
