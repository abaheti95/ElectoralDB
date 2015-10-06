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



def get_upload_file_name(instance, filename):
	print  "uploaded_files/%s_%s"%(str(time()).replace('.',''),filename)
	return "uploaded_files/%s"%(filename)

class Party(models.Model):
    partyid = models.CharField(db_column='Partyid', primary_key=True, max_length=10)  # Field name made lowercase.
    partyname = models.CharField(db_column='PartyName', max_length=50)  # Field name made lowercase.
    symbol = models.FileField(db_column='Symbol', upload_to=get_upload_file_name)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=10)  # Field name made lowercase.
    class Meta:
        db_table = 'Party'
    def __unicode__(self):
        return self.partyid

