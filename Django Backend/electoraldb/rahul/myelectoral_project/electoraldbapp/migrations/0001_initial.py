# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import electoraldbapp.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Party',
            fields=[
                ('partyid', models.CharField(max_length=10, serialize=False, primary_key=True, db_column='Partyid')),
                ('partyname', models.CharField(max_length=50, db_column='PartyName')),
                ('symbol', models.FileField(upload_to=electoraldbapp.models.get_upload_file_name, db_column='Symbol')),
                ('type', models.CharField(max_length=10, db_column='Type')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
