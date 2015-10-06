# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('electoralapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='party',
            table='Party',
        ),
    ]
