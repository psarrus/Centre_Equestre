# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-08 13:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monte', '0010_auto_20160608_1413'),
    ]

    operations = [
        migrations.AlterField(
            model_name='piquetmontoirenseignant',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]