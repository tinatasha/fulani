# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-10-21 12:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='projects',
            field=models.TextField(blank=True),
        ),
    ]