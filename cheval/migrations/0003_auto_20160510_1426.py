# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-10 12:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cheval', '0002_auto_20160510_1408'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emplacement',
            name='emplacement',
            field=models.CharField(choices=[('Emplacement 1', 'Emplacement 1'), ('Emplacement 2', 'Emplacement 2'), ('Emplacement 3', 'Emplacement 3'), ('Emplacement 4', 'Emplacement 4'), ('Emplacement 5', 'Emplacement 5')], max_length=500),
        ),
        migrations.AlterField(
            model_name='status',
            name='status',
            field=models.CharField(choices=[('Propri\xe9t\xe9', 'Propri\xe9t\xe9'), ('Commodat', 'Commodat'), ('Pension', 'Pension'), ('D\xe9bourrage', 'D\xe9bourrage'), ('Divers', 'Divers')], max_length=500),
        ),
    ]