# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-16 02:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_file',
            field=models.FileField(default='', upload_to='./frontend/static/ppt/'),
            preserve_default=False,
        ),
    ]