# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-02-26 07:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Program',
        ),
    ]
