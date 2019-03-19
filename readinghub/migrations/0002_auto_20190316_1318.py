# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-03-16 13:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('readinghub', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Participator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='event',
            name='user',
        ),
        migrations.AddField(
            model_name='book',
            name='image',
            field=models.ImageField(default=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='event',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='event',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='event',
            name='participators',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AddField(
            model_name='participator',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='readinghub.Event'),
        ),
        migrations.AddField(
            model_name='participator',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='readinghub.UserProfile'),
        ),
        migrations.AlterUniqueTogether(
            name='participator',
            unique_together=set([('event', 'user')]),
        ),
    ]