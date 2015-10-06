# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('electoraldbapp', '0004_auto_20150408_2001'),
    ]

    operations = [
        migrations.AddField(
            model_name='polling',
            name='town',
            field=models.CharField(default=0, max_length=50, db_column='Town'),
            preserve_default=False,
        ),
    ]
