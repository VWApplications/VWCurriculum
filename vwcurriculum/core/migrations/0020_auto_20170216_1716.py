# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-16 17:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_auto_20170216_1611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificate',
            name='document',
            field=models.URLField(help_text='URL do google driver do certificado,na imagem clique com o botão direito, depois clique em share e coloque o link no navegador, após isso clique com o botão direito na imagem e copy image address e cole aqui', max_length=1000, verbose_name='URL do certificado'),
        ),
    ]
