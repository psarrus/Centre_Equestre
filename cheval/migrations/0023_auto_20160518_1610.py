# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-18 14:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cheval', '0022_auto_20160511_1410'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cheval',
            old_name='status',
            new_name='statut',
        ),
    ]
