# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-08 09:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('monte', '0008_auto_20160608_1128'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='piquetmontoirenseignant',
            name='montoir',
        ),
        migrations.AddField(
            model_name='piquetmontoirenseignant',
            name='piquet_montoir_staff',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='monte.PiquetMontoirStaff'),
        ),
    ]
