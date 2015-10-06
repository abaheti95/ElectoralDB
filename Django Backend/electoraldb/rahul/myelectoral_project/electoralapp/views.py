from django.shortcuts import render
from django.http import HttpResponse
from electoraldbapp.forms import PartyForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from electoraldbapp.models import Party


def encode(t):
	s = str(t)
	for i in range(0,8-len(s)):
		s = "0"+s
	return s
# Create your views here.
# We make use of the shortcut function to make our lives easier.
def index(request):

    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    context = {}
    return render(request, 'electoraldb/index.html',context)	



def add_party(request):
	# ht
	print "\nin the function\n"
	if request.method == 'POST': 	
		form = PartyForm(request.POST, request.FILES)
		if form.is_valid():
			print "\nis_valid\n"
			party = form.save(commit=False)
			party.partyid = 'PI' + encode(Party.objects.count()+1)
			print "\nhere\n"
			party.save()
			return index(request)			# jump to index.html
		else:
			print "errors ",form.errors
	else:
		#request was not post method type
		form = PartyForm()
	# to render 
	return render(request,'electoraldb/add_party.html',{'form':form})

