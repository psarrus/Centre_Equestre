# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-17 14:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profil', '0012_auto_20160517_1205'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profil',
            name='categorie',
        ),
    ]