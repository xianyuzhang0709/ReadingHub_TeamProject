# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-03-19 20:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('readinghub', '0002_auto_20190316_1318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(blank=True, upload_to='book_images'),
        ),
    ]