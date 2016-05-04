# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-03 22:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0013_auto_20160501_2021'),
    ]

    operations = [
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='games/main_top_image', verbose_name='Top image 1000x600')),
                ('title', models.CharField(blank=True, max_length=49)),
                ('slogan', models.CharField(blank=True, max_length=140)),
            ],
        ),
        migrations.DeleteModel(
            name='TopImage',
        ),
    ]