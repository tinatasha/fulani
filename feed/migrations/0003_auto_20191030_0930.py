# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-10-30 06:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0002_userprofile_projects'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='general_location',
            field=models.TextField(max_length=600, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='neighborhood_name',
            field=models.TextField(max_length=600, null=True),
        ),
    ]