# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-23 03:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stockapp', '0008_history'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='history',
            unique_together=set([('symbol', 'date')]),
        ),
    ]
