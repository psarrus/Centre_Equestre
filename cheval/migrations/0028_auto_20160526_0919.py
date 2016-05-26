# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-26 07:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cheval', '0027_auto_20160524_0904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cheval',
            name='activite',
            field=models.CharField(choices=[('1', 'Monte'), ('2', '\xc9levage')], max_length=1),
        ),
        migrations.AlterField(
            model_name='cheval',
            name='date_sortie',
            field=models.DateField(blank=True, null=True),
        ),
    ]