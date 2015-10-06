# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('electoraldbapp', '0002_auto_20150408_1407'),
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last login')),
                ('candidateid', models.CharField(max_length=10, serialize=False, primary_key=True, db_column='Candidateid')),
                ('voterid', models.CharField(max_length=10, db_column='Voterid')),
                ('acno', models.CharField(max_length=10, db_column='Acno')),
                ('type', models.CharField(default='MLA', max_length=3, choices=[('MP', 'MP'), ('MLA', 'MLA')])),
                ('is_approved', models.BooleanField(default=False)),
                ('partyid', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Candidate',
            },
            bases=(models.Model,),
        ),
    ]
