# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-12-04 14:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0010_auto_20160518_1741'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='about',
            options={'ordering': ['the_order'], 'verbose_name': 'О мастерской', 'verbose_name_plural': '1: О мастерской'},
        ),
    ]