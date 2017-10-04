# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-09-27 15:06
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('diag_app', '0011_auto_20170911_1509'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem',
            name='model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='problems', to='diag_app.Model'),
        ),
        migrations.AlterField(
            model_name='tech',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='tech', to=settings.AUTH_USER_MODEL),
        ),
    ]
