# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-11 11:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cheval', '0018_auto_20160511_1354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emplacement',
            name='box',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
