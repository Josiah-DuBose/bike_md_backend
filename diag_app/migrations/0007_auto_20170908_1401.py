# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-09-08 14:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('diag_app', '0006_auto_20170908_1119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solution',
            name='problem',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='solutions', to='diag_app.Problem'),
        ),
    ]