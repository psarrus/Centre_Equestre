# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-04 18:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profil', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profil',
            name='user',
        ),
        migrations.AddField(
            model_name='profil',
            name='email',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profil',
            name='nom',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profil',
            name='prenom',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
