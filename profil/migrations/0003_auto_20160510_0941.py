# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-10 07:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profil', '0002_auto_20160504_2002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profil',
            name='siret',
            field=models.IntegerField(null=True),
        ),
    ]