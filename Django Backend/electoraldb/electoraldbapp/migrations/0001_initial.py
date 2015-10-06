# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('key', models.CharField(max_length=100, serialize=False, primary_key=True, db_column='key')),
                ('pin', models.IntegerField(db_column='PIN')),
                ('po', models.CharField(max_length=20, db_column='PO')),
                ('town', models.CharField(max_length=50, db_column='Town')),
                ('district', models.CharField(max_length=50, db_column='District')),
                ('state', models.CharField(max_length=50, db_column='State')),
                ('acno', models.CharField(max_length=10, db_column='ACno', blank=True)),
            ],
            options={
                'db_table': 'Address',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('candidateid', models.CharField(max_length=10, serialize=False, primary_key=True, db_column='Candidateid')),
                ('voterid', models.CharField(max_length=10, db_column='Voterid')),
                ('acno', models.CharField(max_length=10, db_column='Acno')),
                ('type', models.CharField(max_length=3, db_column='Type')),
                ('partyid', models.CharField(max_length=10, db_column='Partyid', blank=True)),
                ('password', models.CharField(max_length=60, db_column='Password')),
            ],
            options={
                'db_table': 'Candidate',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Constituency',
            fields=[
                ('acno', models.CharField(max_length=10, serialize=False, primary_key=True, db_column='Acno')),
                ('acname', models.CharField(max_length=50, db_column='Acname')),
                ('population', models.IntegerField(null=True, db_column='Population', blank=True)),
                ('pcno', models.CharField(max_length=10, db_column='PCno', blank=True)),
            ],
            options={
                'db_table': 'Constituency',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DistrictConstituency',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('district', models.CharField(max_length=50, db_column='District')),
                ('acno', models.CharField(max_length=10, db_column='Acno')),
            ],
            options={
                'db_table': 'District_Constituency',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Election',
            fields=[
                ('electionid', models.CharField(max_length=10, serialize=False, primary_key=True, db_column='Electionid')),
                ('year', models.IntegerField()),
            ],
            options={
                'db_table': 'Election',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ElectionStatistics',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('electionid', models.CharField(max_length=10, db_column='Electionid')),
                ('partyid', models.CharField(max_length=10, db_column='Partyid')),
                ('stvotes', models.IntegerField(null=True, db_column='STVotes', blank=True)),
                ('scvotes', models.IntegerField(null=True, db_column='SCVotes', blank=True)),
                ('obcvotes', models.IntegerField(null=True, db_column='OBCVotes', blank=True)),
                ('genvotes', models.IntegerField(null=True, db_column='GENVotes', blank=True)),
                ('femalevotes', models.IntegerField(null=True, db_column='FemaleVotes', blank=True)),
                ('malevotes', models.IntegerField(null=True, db_column='MaleVotes', blank=True)),
            ],
            options={
                'db_table': 'Election_Statistics',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Identity',
            fields=[
                ('picno', models.CharField(max_length=20, serialize=False, primary_key=True, db_column='PICno')),
                ('pictype', models.CharField(max_length=10, db_column='PICtype')),
                ('pic', models.TextField(db_column='PIC', blank=True)),
            ],
            options={
                'db_table': 'Identity',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ParliamentaryConstituency',
            fields=[
                ('pcno', models.CharField(max_length=10, serialize=False, primary_key=True, db_column='PCno')),
                ('pcname', models.CharField(max_length=50, db_column='PCName')),
                ('state', models.CharField(max_length=50, db_column='State')),
            ],
            options={
                'db_table': 'Parliamentary_Constituency',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Party',
            fields=[
                ('partyid', models.CharField(max_length=10, serialize=False, primary_key=True, db_column='Partyid')),
                ('partyname', models.CharField(max_length=50, db_column='PartyName')),
                ('symbol', models.TextField(db_column='Symbol', blank=True)),
                ('type', models.CharField(max_length=10, db_column='Type')),
                ('password', models.CharField(max_length=50, db_column='Password')),
            ],
            options={
                'db_table': 'Party',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PartyCandidate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('partyid', models.CharField(max_length=10, db_column='Partyid')),
                ('voterid', models.CharField(max_length=10, db_column='Voterid')),
            ],
            options={
                'db_table': 'Party_Candidate',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Polling',
            fields=[
                ('partno', models.CharField(max_length=11, serialize=False, primary_key=True, db_column='Partno')),
                ('acno', models.CharField(max_length=10, db_column='Acno')),
            ],
            options={
                'db_table': 'Polling',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Relation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('voterid', models.CharField(max_length=10, db_column='Voterid')),
                ('relationvoterid', models.CharField(max_length=10, db_column='Relationvoterid')),
                ('relation', models.CharField(max_length=10, db_column='Relation')),
            ],
            options={
                'db_table': 'Relation',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Voter',
            fields=[
                ('voterid', models.CharField(max_length=10, serialize=False, primary_key=True, db_column='Voterid')),
                ('name', models.CharField(max_length=50, db_column='Name')),
                ('gender', models.CharField(max_length=6, db_column='Gender')),
                ('dob', models.DateField(db_column='DOB')),
                ('doi', models.DateField(null=True, db_column='DOI', blank=True)),
                ('doa', models.DateField(db_column='DOA')),
                ('emailid', models.CharField(max_length=60, db_column='emailID')),
                ('phoneno', models.IntegerField(db_column='Phoneno')),
                ('picno', models.CharField(max_length=20, db_column='PICno', blank=True)),
                ('houseno', models.CharField(max_length=10, db_column='Houseno')),
                ('streetno', models.CharField(max_length=20, db_column='Streetno')),
                ('town', models.CharField(max_length=50, db_column='Town')),
                ('pin', models.IntegerField(db_column='PIN')),
                ('caste', models.CharField(max_length=3, db_column='Caste')),
                ('partno', models.CharField(max_length=11, db_column='Partno')),
                ('approved', models.CharField(max_length=5, db_column='Approved', blank=True)),
                ('password', models.CharField(max_length=50, db_column='Password')),
            ],
            options={
                'db_table': 'Voter',
            },
            bases=(models.Model,),
        ),
    ]
