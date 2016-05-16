# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-14 13:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarouselObj',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='home/carousel_images', verbose_name='Картинка 1600x1066')),
                ('toptitle', models.CharField(blank=True, max_length=49, verbose_name='Верхняя надпись')),
                ('middletitle', models.CharField(blank=True, max_length=49, verbose_name='Спедняя надпись(большая)')),
                ('bottomtitle', models.CharField(blank=True, max_length=49, verbose_name='Нижняя надпись')),
                ('buttontitle', models.CharField(blank=True, max_length=49, verbose_name='Надпись на кнопке')),
                ('href', models.CharField(blank=True, max_length=49, verbose_name='Ссылка для кнопки')),
                ('the_order', models.PositiveIntegerField(db_index=True, default=0, editable=False)),
            ],
            options={
                'verbose_name_plural': 'Для карусели',
                'ordering': ['the_order'],
                'verbose_name': 'Для карусели',
            },
        ),
        migrations.CreateModel(
            name='TopVideo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=49, verbose_name='Заголовок')),
                ('slogan', models.CharField(blank=True, max_length=49, verbose_name='Девиз')),
                ('video_id', models.CharField(blank=True, max_length=49, verbose_name='Видео (код ютуба)')),
                ('button', models.CharField(blank=True, max_length=49, verbose_name='Надпись на кнопке')),
                ('href', models.CharField(blank=True, max_length=49, verbose_name='Сылка кнопки')),
            ],
            options={
                'verbose_name_plural': 'Видео-заставка',
                'verbose_name': 'Видео-заставка',
            },
        ),
    ]
