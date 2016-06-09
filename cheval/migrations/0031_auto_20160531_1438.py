# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-31 12:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cheval', '0030_merge'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cheval',
            options={'verbose_name_plural': 'Chevaux'},
        ),
        migrations.AlterField(
            model_name='cheval',
            name='emplacement',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='cheval.Emplacement'),
        ),
        migrations.AlterField(
            model_name='cheval',
            name='statut',
            field=models.CharField(choices=[('1', 'Propri\xe9t\xe9'), ('2', 'Commodat'), ('3', 'Pension'), ('4', 'D\xe9bourrage'), ('5', 'Autres')], max_length=1),
        ),
    ]