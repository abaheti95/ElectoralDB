# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import electoraldbapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('electoraldbapp', '0002_auto_20150408_1522'),
    ]

    operations = [
        migrations.AddField(
            model_name='party',
            name='is_approved',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='party',
            name='symbol',
            field=models.FileField(upload_to=electoraldbapp.models.get_upload_file_name, db_column='Symbol'),
        ),
    ]
