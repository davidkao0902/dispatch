# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-11-21 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dispatch', '0004_remove_preview_id_null'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='type',
            field=models.CharField(default='author', max_length=100),
            preserve_default=False,
        ),
    ]
