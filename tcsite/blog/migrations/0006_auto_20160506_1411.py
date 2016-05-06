# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-06 11:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_post_video'),
    ]

    operations = [
        migrations.CreateModel(
            name='TopMedia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('top_image', models.ImageField(upload_to='blog/media')),
                ('title', models.CharField(blank=True, max_length=49)),
                ('slogan', models.CharField(blank=True, max_length=140)),
            ],
        ),
        migrations.AlterField(
            model_name='carousel',
            name='image',
            field=models.ImageField(upload_to='blog/instance/carousel'),
        ),
        migrations.AlterField(
            model_name='post',
            name='video',
            field=models.CharField(blank=True, max_length=21),
        ),
    ]
