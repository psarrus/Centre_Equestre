# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-18 21:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profil', '0015_auto_20160518_2239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profil',
            name='tel_1',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='profil',
            name='tel_2',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='profil',
            name='tel_3',
            field=models.CharField(max_length=10),
        ),
    ]
