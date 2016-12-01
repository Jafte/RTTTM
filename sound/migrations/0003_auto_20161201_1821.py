# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-01 18:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sound', '0002_auto_20161201_1119'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='artistrequest',
            options={'ordering': ['-created']},
        ),
        migrations.AlterModelOptions(
            name='request',
            options={'ordering': ['-created']},
        ),
        migrations.AlterModelOptions(
            name='sound',
            options={'ordering': ['-created']},
        ),
        migrations.AddField(
            model_name='sound',
            name='description',
            field=models.TextField(blank=True, verbose_name='description'),
        ),
    ]
