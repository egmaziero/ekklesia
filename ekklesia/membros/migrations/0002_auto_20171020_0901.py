# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-20 11:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('membros', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='congregacao',
            name='celular',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='congregacao',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='congregacao',
            name='telefone',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]