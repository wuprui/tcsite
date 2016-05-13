# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-13 21:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('map_adress', models.CharField(max_length=140, verbose_name='адрес для карты')),
                ('adress', models.CharField(max_length=154, verbose_name='адрес')),
                ('email', models.CharField(max_length=42, verbose_name='email')),
                ('phone', models.CharField(max_length=21, verbose_name='телефон')),
                ('slogan', models.CharField(blank=True, max_length=700, verbose_name='Девиз')),
            ],
            options={
                'verbose_name_plural': 'Контактная инфа',
                'verbose_name': 'Контактная инфа',
            },
        ),
    ]