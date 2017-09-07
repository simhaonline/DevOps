# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-17 10:16
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('operation', '0007_remove_script_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='script',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
    ]