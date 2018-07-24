# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-24 08:37
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('doto', '0002_auto_20180723_1658'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='todo',
            name='status',
            field=models.CharField(choices=[('Todo', 'Todo'), ('Doing', 'Doing'), ('Done', 'Done')], max_length=5),
        ),
    ]
