# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-08 14:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profil', '0028_profil_permis'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profil',
            name='permis',
            field=models.CharField(blank=True, choices=[('chef_ecurie', "Chef d'\xe9curie"), ('professeur', 'Professeur')], default='', max_length=30),
        ),
    ]