# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-01 08:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0009_auto_20160501_1101'),
    ]

    operations = [
        migrations.CreateModel(
            name='TopVideo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=49)),
                ('slogan', models.CharField(blank=True, max_length=49)),
                ('video_id', models.CharField(blank=True, max_length=49)),
            ],
        ),
    ]