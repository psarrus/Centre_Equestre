# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-31 07:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monte', '0003_auto_20160519_1553'),
    ]

    operations = [
        migrations.AddField(
            model_name='piquetmontoirstaff',
            name='selected',
            field=models.BooleanField(default=False),
        ),
    ]