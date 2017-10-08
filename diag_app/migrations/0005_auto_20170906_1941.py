# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-09-06 19:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('diag_app', '0004_auto_20170831_1134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solution',
            name='problem',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='solutions', to='diag_app.Problem'),
        ),
    ]