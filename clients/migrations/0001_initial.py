# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-05 07:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('phone', models.IntegerField(unique=True)),
                ('email', models.EmailField(max_length=250)),
                ('address', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
