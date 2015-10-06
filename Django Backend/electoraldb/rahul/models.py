# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

class Address(models.Model):
    pin = models.IntegerField(db_column='PIN')  # Field name made lowercase.
    po = models.CharField(db_column='PO', max_length=20)  # Field name made lowercase.
    town = models.CharField(db_column='Town', max_length=50)  # Field name made lowercase.
    district = models.CharField(db_column='District', max_length=50)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=50)  # Field name made lowercase.
    acno = models.ForeignKey('Constituency', db_column='ACno', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'Address'
    def __unicode__(self):
        return str(self.pin)+" : "+ self.town


class Candidate(models.Model):
    candidateid = models.CharField(db_column='Candidateid', primary_key=True, max_length=10)  # Field name made lowercase.
    voterid = models.ForeignKey('Voter', db_column='Voterid')  # Field name made lowercase.
    acno = models.ForeignKey('Constituency', db_column='Acno')  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=3)  # Field name made lowercase.
    partyid = models.ForeignKey('Party', db_column='Partyid', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'Candidate'

    def __unicode__(self):
        return self.candidateid


class Constituency(models.Model):
    acno = models.CharField(db_column='Acno', primary_key=True, max_length=10)  # Field name made lowercase.
    acname = models.CharField(db_column='Acname', max_length=50)  # Field name made lowercase.
    population = models.IntegerField(db_column='Population', blank=True, null=True)  # Field name made lowercase.
    pcno = models.ForeignKey('ParliamentaryConstituency', db_column='PCno', blank=True, null=True)  # Field name made lowercase.

    class Meta: 
        db_table = 'Constituency'

    def __unicode__(self):
        return self.acno


class DistrictConstituency(models.Model):
    district = models.CharField(db_column='District', max_length=50)  # Field name made lowercase.
    acno = models.ForeignKey(Constituency, db_column='Acno')  # Field name made lowercase.

    class Meta:
        db_table = 'District_Constituency'

    def __unicode__(self):
        return self.district+":"+self.acno


class Election(models.Model):
    electionid = models.CharField(db_column='Electionid', primary_key=True, max_length=10)  # Field name made lowercase.
    year = models.IntegerField()

    class Meta:
        db_table = 'Election'
    def __unicode__(self):
        return self.electionid


class ElectionStatistics(models.Model):
    electionid = models.ForeignKey(Election, db_column='Electionid')  # Field name made lowercase.
    partyid = models.ForeignKey('Party', db_column='Partyid')  # Field name made lowercase.
    stvotes = models.IntegerField(db_column='STVotes', blank=True, null=True)  # Field name made lowercase.
    scvotes = models.IntegerField(db_column='SCVotes', blank=True, null=True)  # Field name made lowercase.
    obcvotes = models.IntegerField(db_column='OBCVotes', blank=True, null=True)  # Field name made lowercase.
    genvotes = models.IntegerField(db_column='GENVotes', blank=True, null=True)  # Field name made lowercase.
    femalevotes = models.IntegerField(db_column='FemaleVotes', blank=True, null=True)  # Field name made lowercase.
    malevotes = models.IntegerField(db_column='MaleVotes', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'Election_Statistics'
    def __unicode__(self):
        return self.electionid+"::"+self.partyid

class Identity(models.Model):
    picno = models.CharField(db_column='PICno', primary_key=True, max_length=20)  # Field name made lowercase.
    pictype = models.CharField(db_column='PICtype', max_length=10)  # Field name made lowercase.
    pic = models.TextField(db_column='PIC')  # Field name made lowercase.

    class Meta:
        db_table = 'Identity'

    def __unicode__(self):
        return self.picno


class ParliamentaryConstituency(models.Model):
    pcno = models.CharField(db_column='PCno', primary_key=True, max_length=10)  # Field name made lowercase.
    pcname = models.CharField(db_column='PCName', max_length=50)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=50)  # Field name made lowercase.

    class Meta:
        db_table = 'Parliamentary_Constituency'

    def __unicode__(self):
        return self.pcno+" : "+self.pcname


class Party(models.Model):
    partyid = models.CharField(db_column='Partyid', primary_key=True, max_length=10)  # Field name made lowercase.
    partyname = models.CharField(db_column='PartyName', max_length=50, unique = True)  # Field name made lowercase.
    symbol = models.TextField(db_column='Symbol', blank=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=10)  # Field name made lowercase.

    class Meta:
        db_table = 'Party'

    def __unicode__(self):
        return self.partyid


class PartyCandidate(models.Model):
    partyid = models.CharField(db_column='Partyid', max_length=10)  # Field name made lowercase.
    voterid = models.CharField(db_column='Voterid', max_length=10)  # Field name made lowercase.

    class Meta:
        db_table = 'Party_Candidate'

    def __unicode__(self):
        return self.voterid + " : " + self.partyid


class Polling(models.Model):
    partno = models.CharField(db_column='Partno', primary_key=True, max_length=11)  # Field name made lowercase.
    acno = models.ForeignKey(Constituency, db_column='Acno')  # Field name made lowercase.

    class Meta:
        db_table = 'Polling'

    def __unicode__(self):
        return self.partno+" : "+self.acno

class Relation(models.Model):
    voterid = models.CharField(db_column='Voterid', max_length=10)  # Field name made lowercase.
    relationvoterid = models.CharField(db_column='Relationvoterid', max_length=10)  # Field name made lowercase.
    relation = models.CharField(db_column='Relation', max_length=10)  # Field name made lowercase.

    class Meta:
        db_table = 'Relation'

    def __unicode__(self):
        return self.relationvoterid + " : " +self.relation


class Voter(models.Model):
    voterid = models.CharField(db_column='Voterid', primary_key=True, max_length=10)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50)  # Field name made lowercase.
    age = models.IntegerField(db_column='Age')  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=6)  # Field name made lowercase.
    dob = models.DateField(db_column='DOB')  # Field name made lowercase.
    doi = models.DateField(db_column='DOI', blank=True, null=True)  # Field name made lowercase.
    doa = models.DateField(db_column='DOA', blank=True, null=True)  # Field name made lowercase.
    emailid = models.CharField(db_column='emailID', max_length=60, blank=True)  # Field name made lowercase.
    phoneno = models.IntegerField(db_column='Phoneno', blank=True, null=True)  # Field name made lowercase.
    picno = models.CharField(db_column='PICno',max_length=20, blank=True,null=True)  # Field name made lowercase.
    houseno = models.IntegerField(db_column='Houseno')  # Field name made lowercase.
    streetno = models.CharField(db_column='Streetno', max_length=20)  # Field name made lowercase.
    town = models.ForeignKey(Address, db_column='Town',related_name='+')  # Field name made lowercase.
    pin = models.ForeignKey(Address, db_column='PIN')  # Field name made lowercase.
    caste = models.CharField(db_column='Caste', max_length=3)  # Field name made lowercase.
    partno = models.CharField(db_column='Partno',blank=True,max_length=10,null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'Voter'

    def __unicode__(self):
        return self.name
