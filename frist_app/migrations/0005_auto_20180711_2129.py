# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-07-11 21:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frist_app', '0004_auto_20180710_2106'),
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('frist_Name', models.CharField(default='SOME STRING', max_length=20)),
                ('last_Name', models.CharField(default='SOME STRING', max_length=20)),
                ('email', models.EmailField(default='SOME STRING', max_length=50, unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='userdata',
            name='topic',
        ),
        migrations.DeleteModel(
            name='userData',
        ),
    ]
