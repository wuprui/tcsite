# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-01 13:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0003_auto_20160429_0014'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(upload_to='', verbose_name='Avatar 600x820')),
                ('name', models.CharField(max_length=49)),
                ('speech', models.CharField(max_length=210)),
                ('member_order', models.PositiveIntegerField(db_index=True, default=0, editable=False)),
            ],
            options={
                'verbose_name_plural': 'ClientReviews',
                'ordering': ['member_order'],
                'verbose_name': 'ClientReview',
            },
        ),
        migrations.AlterField(
            model_name='about',
            name='preview_image',
            field=models.ImageField(upload_to='', verbose_name='Top image 1600x1067'),
        ),
        migrations.AlterField(
            model_name='teammember',
            name='image',
            field=models.ImageField(upload_to='', verbose_name='Member photo 600x820'),
        ),
        migrations.AddField(
            model_name='clientreview',
            name='about',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='about.About'),
        ),
    ]