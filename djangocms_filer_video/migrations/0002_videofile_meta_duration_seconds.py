# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-11-08 09:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_filer_video', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='videofile',
            name='meta_duration_seconds',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='duration'),
        ),
    ]
