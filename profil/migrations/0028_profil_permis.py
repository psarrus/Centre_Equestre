# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-08 14:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profil', '0027_auto_20160608_1427'),
    ]

    operations = [
        migrations.AddField(
            model_name='profil',
            name='permis',
            field=models.CharField(blank=True, choices=[('1', "Chef d'\xe9curie"), ('2', 'Professeur')], default='', max_length=30),
        ),
    ]
