# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-09 14:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profil', '0041_auto_20160609_1423'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profil',
            name='permis',
            field=models.CharField(blank=True, choices=[('1', 'Professeur'), ('2', "Chef d'\xe9curie")], default='1', max_length=30, null=True),
        ),
    ]
