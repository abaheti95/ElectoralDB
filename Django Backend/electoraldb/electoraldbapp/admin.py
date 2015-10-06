from django.contrib import admin
from electoraldbapp.models import Address,Constituency,Voter,Party,Candidate,Polling
# Register your models here.
admin.site.register(Address)
admin.site.register(Constituency)
admin.site.register(Voter)
admin.site.register(Party)
admin.site.register(Candidate)
admin.site.register(Polling)
