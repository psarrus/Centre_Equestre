# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-26 11:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profil', '0019_auto_20160526_1337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='periode',
            name='debut',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='periode',
            name='fin',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='periode',
            name='license',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
    ]