# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-06-25 15:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('diag_app', '0004_auto_20170330_1221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commit',
            name='solution',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='diag_app.Solution'),
        ),
        migrations.AlterField(
            model_name='notification',
            name='commit',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='diag_app.Commit'),
        ),
        migrations.AlterField(
            model_name='notification',
            name='solution',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='diag_app.Solution'),
        ),
        migrations.AlterField(
            model_name='notification',
            name='tech',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='diag_app.Tech'),
        ),
        migrations.AlterField(
            model_name='problem',
            name='system',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='diag_app.System'),
        ),
        migrations.AlterField(
            model_name='problem',
            name='tech',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='diag_app.Tech'),
        ),
        migrations.AlterField(
            model_name='solution',
            name='problem',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='diag_app.Problem'),
        ),
        migrations.AlterField(
            model_name='solution',
            name='tech',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='diag_app.Tech'),
        ),
        migrations.AlterField(
            model_name='vote',
            name='solution',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='diag_app.Solution'),
        ),
    ]
