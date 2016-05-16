# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-14 14:00
from __future__ import unicode_literals

import adminsortable.fields
import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AllTags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tags', models.CharField(max_length=140, verbose_name='Тэги через "," без пробелов')),
            ],
            options={
                'verbose_name_plural': 'Тэги для подменю',
                'verbose_name': 'Тэги для подменю',
            },
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='works/main_top_image', verbose_name='Картинка 1600 на 1060')),
                ('title', models.CharField(blank=True, max_length=49, verbose_name='Заголовок')),
                ('slogan', models.CharField(blank=True, max_length=140, verbose_name='Девиз')),
            ],
            options={
                'verbose_name_plural': 'Заставка для работ',
                'verbose_name': 'Заставка для работ',
            },
        ),
        migrations.CreateModel(
            name='Screenshot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('screenshot_image', models.ImageField(upload_to='works/instance', verbose_name='Картинка 1000 на 600')),
                ('screenshot_order', models.PositiveIntegerField(db_index=True, default=0, editable=False)),
            ],
            options={
                'verbose_name_plural': 'Картинки 1000 на 600',
                'verbose_name': 'Картинка 1000 на 600',
                'ordering': ['screenshot_order'],
            },
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('top_image', models.ImageField(upload_to='works/top_images', verbose_name='Картинка-заставка 1600 на 1066')),
                ('name', models.CharField(max_length=49, verbose_name='Название работы (крупное на заставке)')),
                ('preview_image', models.ImageField(upload_to='works/preview_images', verbose_name='Картинка предпросмотра 800 на 600')),
                ('slogan', models.CharField(blank=True, max_length=140, verbose_name='Девиз заставки')),
                ('text0', ckeditor.fields.RichTextField(blank=True, verbose_name='Верхний текстовый блок')),
                ('video_id', models.CharField(blank=True, max_length=49, verbose_name='Видео (код ютуба)')),
                ('text1', ckeditor.fields.RichTextField(blank=True, verbose_name='Средний текстовый блок (под видео)')),
                ('text2', ckeditor.fields.RichTextField(blank=True, verbose_name='Нижний текстовый блок (под каруселью)')),
                ('client', models.CharField(blank=True, max_length=49, verbose_name='Для клиента: ')),
                ('tags', models.CharField(blank=True, max_length=70, verbose_name='Тэги работы')),
                ('work_order', models.PositiveIntegerField(db_index=True, default=0, editable=False)),
            ],
            options={
                'verbose_name_plural': 'Работы',
                'verbose_name': 'Работа',
                'ordering': ['work_order'],
            },
        ),
        migrations.AddField(
            model_name='screenshot',
            name='game',
            field=adminsortable.fields.SortableForeignKey(on_delete=django.db.models.deletion.CASCADE, to='works.Work'),
        ),
    ]
