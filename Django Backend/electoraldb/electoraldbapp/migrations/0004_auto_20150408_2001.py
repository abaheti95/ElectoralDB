# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('electoraldbapp', '0003_auto_20150408_1830'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='is_approved',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='candidate',
            name='partyid',
            field=models.ForeignKey(to='electoraldbapp.Party'),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='password',
            field=models.CharField(max_length=50, db_column='Password'),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='type',
            field=models.CharField(default='MLA', max_length=3, choices=[('MP', 'MP'), ('MLA', 'MLA')]),
        ),
    ]
