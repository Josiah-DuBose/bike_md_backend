# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2018-05-30 00:27
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('make_id', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Commit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('posted', models.DateTimeField(auto_now=True)),
                ('text', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('weight', models.IntegerField(default=0)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='diag_app.Brand')),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=20)),
                ('posted', models.DateTimeField(auto_now=True)),
                ('commit', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='diag_app.Commit')),
            ],
        ),
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=65)),
                ('system', models.CharField(max_length=20)),
                ('description', models.TextField(max_length=500)),
                ('posted', models.DateTimeField(auto_now=True)),
                ('mileage', models.IntegerField(default=0)),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='problems', to='diag_app.Model')),
            ],
        ),
        migrations.CreateModel(
            name='Solution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(max_length=500)),
                ('time_required', models.FloatField(default=0)),
                ('parts_cost', models.DecimalField(decimal_places=2, max_digits=6)),
                ('posted', models.DateTimeField(auto_now=True)),
                ('score', models.IntegerField(default=0)),
                ('problem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='solutions', to='diag_app.Problem')),
            ],
        ),
        migrations.CreateModel(
            name='Tech',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('experience', models.IntegerField(default=0)),
                ('job_title', models.CharField(max_length=25, null=True)),
                ('shop', models.CharField(max_length=25, null=True)),
                ('tech_rating', models.IntegerField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='tech', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Year',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=4)),
            ],
        ),
        migrations.AddField(
            model_name='solution',
            name='tech',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='diag_app.Tech'),
        ),
        migrations.AddField(
            model_name='problem',
            name='tech',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='diag_app.Tech'),
        ),
        migrations.AddField(
            model_name='notification',
            name='solution',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='diag_app.Solution'),
        ),
        migrations.AddField(
            model_name='notification',
            name='tech',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='diag_app.Tech'),
        ),
        migrations.AddField(
            model_name='model',
            name='year',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='diag_app.Year'),
        ),
        migrations.AddField(
            model_name='commit',
            name='solution',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='diag_app.Solution'),
        ),
        migrations.AddField(
            model_name='commit',
            name='tech',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='diag_app.Tech'),
        ),
    ]
