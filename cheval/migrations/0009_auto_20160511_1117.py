# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-11 09:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cheval', '0008_cheval_emplacement'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='adresse',
            name='cheval',
        ),
        migrations.RemoveField(
            model_name='adresse',
            name='emplacement',
        ),
        migrations.DeleteModel(
            name='Adresse',
        ),
    ]
