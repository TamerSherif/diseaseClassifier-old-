# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-26 19:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0005_test'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fileupload',
            name='uploaded_at',
        ),
    ]