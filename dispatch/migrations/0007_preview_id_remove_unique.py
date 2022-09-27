# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-12 09:21

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('dispatch', '0006_author_many_to_many'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='preview_id',
            field=models.UUIDField(default=uuid.uuid4),
        ),
        migrations.AlterField(
            model_name='page',
            name='preview_id',
            field=models.UUIDField(default=uuid.uuid4),
        ),
    ]
