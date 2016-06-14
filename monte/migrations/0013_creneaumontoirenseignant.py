# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-09 09:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profil', '0033_auto_20160608_1641'),
        ('monte', '0012_auto_20160608_1600'),
    ]

    operations = [
        migrations.CreateModel(
            name='CreneauMontoirEnseignant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True)),
                ('heure_debut', models.TimeField()),
                ('duree', models.FloatField()),
                ('effectif', models.CharField(max_length=65)),
                ('remarque', models.TextField(blank=True)),
                ('encadrant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profil.Profil')),
                ('public', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profil.Public')),
            ],
        ),
    ]