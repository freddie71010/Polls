# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-14 15:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='section',
            field=models.CharField(choices=[('wip', 'wip'), ('completed', 'completed'), ('future', 'future')], default='Blank', max_length=100),
        ),
    ]
