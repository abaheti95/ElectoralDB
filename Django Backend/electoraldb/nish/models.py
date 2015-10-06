from __future__ import unicode_literals

from django.db import models


class Address(models.Model):
    pin = models.IntegerField(db_column='PIN')  # Field name made lowercase.
    po = models.CharField(db_column='PO', max_length=20)  # Field name made lowercase.
    town = models.CharField(db_column='Town', max_length=50)  # Field name made lowercase.
    district = models.CharField(db_column='District', max_length=50)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=50)  # Field name made lowercase.
    acno = models.CharField(db_column='ACno', max_length=10, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Address'


class Candidate(models.Model):
    candidateid = models.CharField(db_column='Candidateid', primary_key=True, max_length=10)  # Field name made lowercase.
    voterid = models.CharField(db_column='Voterid', max_length=10)  # Field name made lowercase.
    acno = models.CharField(db_column='Acno', max_length=10)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=3)  # Field name made lowercase.
    partyid = models.CharField(db_column='Partyid', max_length=10, blank=True)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=60)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Candidate'


class Constituency(models.Model):
    acno = models.CharField(db_column='Acno', primary_key=True, max_length=10)  # Field name made lowercase.
    acname = models.CharField(db_column='Acname', max_length=50)  # Field name made lowercase.
    population = models.IntegerField(db_column='Population', blank=True, null=True)  # Field name made lowercase.
    pcno = models.CharField(db_column='PCno', max_length=10, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Constituency'


class DistrictConstituency(models.Model):
    district = models.CharField(db_column='District', max_length=50)  # Field name made lowercase.
    acno = models.CharField(db_column='Acno', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'District_Constituency'


class Election(models.Model):
    electionid = models.CharField(db_column='Electionid', primary_key=True, max_length=10)  # Field name made lowercase.
    year = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'Election'


class ElectionStatistics(models.Model):
    electionid = models.CharField(db_column='Electionid', max_length=10)  # Field name made lowercase.
    partyid = models.CharField(db_column='Partyid', max_length=10)  # Field name made lowercase.
    stvotes = models.IntegerField(db_column='STVotes', blank=True, null=True)  # Field name made lowercase.
    scvotes = models.IntegerField(db_column='SCVotes', blank=True, null=True)  # Field name made lowercase.
    obcvotes = models.IntegerField(db_column='OBCVotes', blank=True, null=True)  # Field name made lowercase.
    genvotes = models.IntegerField(db_column='GENVotes', blank=True, null=True)  # Field name made lowercase.
    femalevotes = models.IntegerField(db_column='FemaleVotes', blank=True, null=True)  # Field name made lowercase.
    malevotes = models.IntegerField(db_column='MaleVotes', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Election_Statistics'


class Identity(models.Model):
    picno = models.CharField(db_column='PICno', primary_key=True, max_length=20)  # Field name made lowercase.
    pictype = models.CharField(db_column='PICtype', max_length=10)  # Field name made lowercase.
    pic = models.TextField(db_column='PIC', blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Identity'


class ParliamentaryConstituency(models.Model):
    pcno = models.CharField(db_column='PCno', primary_key=True, max_length=10)  # Field name made lowercase.
    pcname = models.CharField(db_column='PCName', max_length=50)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Parliamentary_Constituency'


class Party(models.Model):
    partyid = models.CharField(db_column='Partyid', primary_key=True, max_length=10)  # Field name made lowercase.
    partyname = models.CharField(db_column='PartyName', max_length=50)  # Field name made lowercase.
    symbol = models.TextField(db_column='Symbol', blank=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=10)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Party'


class PartyCandidate(models.Model):
    partyid = models.CharField(db_column='Partyid', max_length=10)  # Field name made lowercase.
    voterid = models.CharField(db_column='Voterid', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Party_Candidate'


class Polling(models.Model):
    partno = models.CharField(db_column='Partno', primary_key=True, max_length=11)  # Field name made lowercase.
    acno = models.CharField(db_column='Acno', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Polling'


class Relation(models.Model):
    voterid = models.CharField(db_column='Voterid', max_length=10)  # Field name made lowercase.
    relationvoterid = models.CharField(db_column='Relationvoterid', max_length=10)  # Field name made lowercase.
    relation = models.CharField(db_column='Relation', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Relation'


class Voter(models.Model):
    voterid = models.CharField(db_column='Voterid', primary_key=True, max_length=10)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=50) 
    age = models.IntegerField(db_column='Age')  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=6)  # Field name made lowercase.
    dob = models.DateField(db_column='DOB')  # Field name made lowercase.
    doi = models.DateField(db_column='DOI', blank=True, null=True)  # Field name made lowercase.
    doa = models.DateField(db_column='DOA')  # Field name made lowercase.
    emailid = models.CharField(db_column='emailID', max_length=60)  # Field name made lowercase.
    phoneno = models.IntegerField(db_column='Phoneno')  # Field name made lowercase.
    picno = models.CharField(db_column='PICno', max_length=20, blank=True)  # Field name made lowercase.
    houseno = models.CharField(db_column='Houseno', max_length=10)  # Field name made lowercase.
    streetno = models.CharField(db_column='Streetno', max_length=20)  # Field name made lowercase.
    town = models.CharField(db_column='Town', max_length=50)  # Field name made lowercase.
    pin = models.IntegerField(db_column='PIN')  # Field name made lowercase.
    caste = models.CharField(db_column='Caste', max_length=3)  # Field name made lowercase.
    partno = models.CharField(db_column='Partno', max_length=11)  # Field name made lowercase.
    approved = models.CharField(db_column='Approved', max_length=5, blank=True)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Voter'
