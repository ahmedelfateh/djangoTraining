# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-07-10 21:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frist_app', '0003_userdata'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdata',
            name='name',
        ),
        migrations.AddField(
            model_name='userdata',
            name='email',
            field=models.EmailField(default='SOME STRING', max_length=50, unique=True),
        ),
        migrations.AddField(
            model_name='userdata',
            name='frist_Name',
            field=models.CharField(default='SOME STRING', max_length=20),
        ),
        migrations.AddField(
            model_name='userdata',
            name='last_Name',
            field=models.CharField(default='SOME STRING', max_length=20),
        ),
    ]
