# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-10 07:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profil', '0044_auto_20160609_1616'),
        ('monte', '0017_auto_20160609_1428'),
    ]

    operations = [
        migrations.AddField(
            model_name='creneaumontoirenseignant',
            name='encadrant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='profil.Profil'),
        ),
    ]