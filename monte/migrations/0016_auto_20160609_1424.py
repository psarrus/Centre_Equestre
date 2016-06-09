# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-09 12:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('monte', '0015_auto_20160609_1202'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='creneaumontoirenseignant',
            name='duree',
        ),
        migrations.RemoveField(
            model_name='creneaumontoirenseignant',
            name='effectif',
        ),
        migrations.RemoveField(
            model_name='creneaumontoirenseignant',
            name='encadrant',
        ),
        migrations.RemoveField(
            model_name='creneaumontoirenseignant',
            name='heure_debut',
        ),
        migrations.RemoveField(
            model_name='creneaumontoirenseignant',
            name='public',
        ),
        migrations.RemoveField(
            model_name='creneaumontoirenseignant',
            name='remarque',
        ),
        migrations.AddField(
            model_name='creneaumontoirenseignant',
            name='creneau_montoir',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='monte.CreneauMontoir'),
        ),
    ]
