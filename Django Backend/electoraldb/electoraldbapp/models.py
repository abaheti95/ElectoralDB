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
from django.shortcuts import render
from django.http import HttpResponse
from django.db import models
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.models import Group
from django.contrib.auth.models import Group, Permission
from django.contrib.auth.models import Permission, User
from django.shortcuts import get_object_or_404
from time import time

def get_upload_file_name(instance, filename):
	return "uploaded_files/%s_%s"%(str(time()).replace('.',''),filename)

class Address(models.Model):
	key = models.CharField(db_column='key',max_length=100,primary_key=True)
	pin = models.IntegerField(db_column='PIN')  # Field name made lowercase.
	po = models.CharField(db_column='PO', max_length=20)  # Field name made lowercase.
	town = models.CharField(db_column='Town', max_length=50)  # Field name made lowercase.
	district = models.CharField(db_column='District', max_length=50)  # Field name made lowercase.
	state = models.CharField(db_column='State', max_length=50)  # Field name made lowercase.
	acno = models.CharField(db_column='ACno', max_length=10, blank=True)  # Field name made lowercase.

	class Meta:
		db_table = 'Address'
	def __unicode__(self):
		return self.key




class Constituency(models.Model):
	acno = models.CharField(db_column='Acno', primary_key=True, max_length=10)  # Field name made lowercase.
	acname = models.CharField(db_column='Acname', max_length=50)  # Field name made lowercase.
	population = models.IntegerField(db_column='Population', blank=True, null=True)  # Field name made lowercase.
	pcno = models.CharField(db_column='PCno', max_length=10, blank=True)  # Field name made lowercase.

	class Meta:
		db_table = 'Constituency'
	def __unicode__(self):
		return self.acname

class DistrictConstituency(models.Model):
	district = models.CharField(db_column='District', max_length=50)  # Field name made lowercase.
	acno = models.CharField(db_column='Acno', max_length=10)  # Field name made lowercase.

	class Meta:
		db_table = 'District_Constituency'
	def __unicode__(self):
		return self.district



class Election(models.Model):
	electionid = models.CharField(db_column='Electionid', primary_key=True, max_length=10)  # Field name made lowercase.
	year = models.IntegerField()

	class Meta:
		db_table = 'Election'
	def __unicode__(self):
		return self.electionid



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
		db_table = 'Election_Statistics'
	def __unicode__(self):
		return self.electionid



class Identity(models.Model):
	picno = models.CharField(db_column='PICno', primary_key=True, max_length=20)  # Field name made lowercase.
	pictype = models.CharField(db_column='PICtype', max_length=10)  # Field name made lowercase.
	pic = models.TextField(db_column='PIC', blank=True)  # Field name made lowercase.

	class Meta:
		db_table = 'Identity'



class ParliamentaryConstituency(models.Model):
	pcno = models.CharField(db_column='PCno', primary_key=True, max_length=10)  # Field name made lowercase.
	pcname = models.CharField(db_column='PCName', max_length=50)  # Field name made lowercase.
	state = models.CharField(db_column='State', max_length=50)  # Field name made lowercase.

	class Meta:
		db_table = 'Parliamentary_Constituency'
	def __unicode__(self):
		return self.pcname


class Party(models.Model):
	partyid = models.CharField(db_column='Partyid', primary_key=True, max_length=10)  # Field name made lowercase.
	partyname = models.CharField(db_column='PartyName', max_length=50)  # Field name made lowercase.
	symbol = models.FileField(db_column='Symbol', upload_to=get_upload_file_name)  # Field name made lowercase.
	type = models.CharField(db_column='Type', max_length=10)  # Field name made lowercase.
	password = models.CharField(db_column='Password', max_length=50)  # Field name made lowercase.
	is_approved = models.BooleanField(default=False)
	def __unicode__(self):
		return self.partyid


	class Meta:
		db_table = 'Party'

class Candidate(models.Model):
	candidateid = models.CharField(db_column='Candidateid', primary_key=True, max_length=10)  
	voterid = models.CharField(db_column='Voterid', max_length=10)  							# foreign key valdated in views.py
	acno = models.CharField(db_column='Acno', max_length=10)   									# foreign key taken care during rendering
	type = models.CharField(max_length=3, choices=(('MP','MP'),('MLA','MLA')),default='MLA')      # Field name made lowercase.
	partyid = models.ForeignKey(Party)
	password = models.CharField(db_column='Password', max_length=50)  # Field name made lowercase.
	is_approved = models.BooleanField(default=False)
	class Meta:
		db_table = 'Candidate'
	def __unicode__(self):
		return self.candidateid


class PartyCandidate(models.Model):
	partyid = models.CharField(db_column='Partyid', max_length=10)  # Field name made lowercase.
	voterid = models.CharField(db_column='Voterid', max_length=10)  # Field name made lowercase.

	class Meta:
		db_table = 'Party_Candidate'


class Polling(models.Model):
	town = models.CharField(db_column='Town', max_length=50)  # Field name made lowercase.ade lowercase.
	partno = models.CharField(db_column='Partno', primary_key=True, max_length=11)  # Field name made lowercase.
	acno = models.CharField(db_column='Acno', max_length=10)  # Field name made lowercase.

	class Meta:
		db_table = 'Polling'
	def __unicode__(self):
		return self.town



class Relation(models.Model):
	voterid = models.CharField(db_column='Voterid', max_length=10)  # Field name made lowercase.
	relationvoterid = models.CharField(db_column='Relationvoterid', max_length=10)  # Field name made lowercase.
	relation = models.CharField(db_column='Relation', max_length=10)  # Field name made lowercase.

	class Meta:
		db_table = 'Relation'


class Voter(models.Model):
	voterid = models.CharField(db_column='Voterid', primary_key=True, max_length=10)  	# Field name made lowercase.
	name = models.CharField(db_column='Name', max_length=50)  							# Field name made lowercase.
	gender = models.CharField(db_column='Gender', max_length=6)  						# Field name made lowercase.
	dob = models.DateField(db_column='DOB')  											# Field name made lowercase.
	doi = models.DateField(db_column='DOI', blank=True, null=True)  					# Field name made lowercase.
	doa = models.DateField(db_column='DOA')  											# Field name made lowercase.
	emailid = models.CharField(db_column='emailID', max_length=60)  					# Field name made lowercase.
	phoneno = models.BigIntegerField(db_column='Phoneno')  								# Field name made lowercase.
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
		db_table = 'Voter'
	def __unicode__(self):
		return self.voterid

