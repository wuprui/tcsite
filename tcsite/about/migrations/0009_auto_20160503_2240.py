# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-03 19:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0008_about_middle_bg'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ClientReview',
            new_name='Review',
        ),
    ]