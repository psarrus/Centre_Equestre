# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-31 13:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sante', '0006_auto_20160531_1438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registresoins',
            name='acte',
            field=models.CharField(choices=[('1', 'Soin'), ('2', 'Vaccin'), ('3', 'Ferrage'), ('4', 'Vermifugation'), ('5', 'Autres')], max_length=1),
        ),
    ]