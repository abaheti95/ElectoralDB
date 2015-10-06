# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('electoraldbapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='party',
            name='is_approved',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='party',
            name='last_login',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='last login'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='party',
            name='password',
            field=models.CharField(default=-2011, max_length=128, verbose_name='password'),
            preserve_default=False,
        ),
    ]
