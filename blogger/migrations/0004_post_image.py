# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-16 14:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogger', '0003_post_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]
