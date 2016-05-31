# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-31 12:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sante', '0005_auto_20160519_0950'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='registresoins',
            options={'verbose_name': 'Soin', 'verbose_name_plural': 'Soins'},
        ),
        migrations.AlterField(
            model_name='registresoins',
            name='acte',
            field=models.CharField(choices=[('1', 'Soin'), ('2', 'Vaccin'), ('3', 'Vermifugation'), ('4', 'Ferrage'), ('5', 'Autres')], max_length=1),
        ),
        migrations.AlterField(
            model_name='registresoins',
            name='pathologie',
            field=models.CharField(max_length=100),
        ),
    ]
