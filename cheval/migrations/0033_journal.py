# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-09 10:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cheval', '0032_auto_20160531_1646'),
    ]

    operations = [
        migrations.CreateModel(
            name='Journal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('motif', models.CharField(max_length=100)),
                ('lieu', models.CharField(max_length=100)),
                ('cheval', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cheval.Cheval')),
            ],
        ),
    ]
