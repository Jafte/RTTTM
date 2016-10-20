# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-18 16:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='name')),
                ('about', models.TextField(blank=True, verbose_name='about')),
            ],
        ),
        migrations.CreateModel(
            name='Text',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='name')),
                ('url_to_source', models.CharField(blank=True, max_length=200, verbose_name='url to source')),
                ('text', models.TextField(verbose_name='text')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modified')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='texts', to='text.Author', verbose_name='author')),
            ],
        ),
    ]
