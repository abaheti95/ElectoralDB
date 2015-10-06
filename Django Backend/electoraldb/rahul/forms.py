from django import forms
from electoraldbapp.models import Address, Constituency, Voter, Polling, Party, Candidate
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import datetime
import html5.forms.widgets as html5_widgets

forms.DateInput.input_type="date"
forms.DateTimeInput.input_type="datetime-local" 
def encode(t):
	s = str(t)
	for i in range(0,8-len(s)):
		s = "0"+s
	return s

class AddressForm(forms.ModelForm):
	pin = forms.IntegerField(help_text="Please enter the pincode")# Field name made lowercase.
	po = forms.CharField(max_length=20,help_text="Post office?")  # Field name made lowercase.
	town = forms.CharField(max_length=50,help_text="Town?")  # Field name made lowercase.
	district = forms.CharField(max_length=50,help_text="District?")  # Field name made lowercase.
	state = forms.CharField(max_length=50,help_text="state?")  # Field name made lowercase.
	acno = forms.ModelChoiceField(queryset=Constituency.objects.all())  # Field name made lowercase.

	class Meta:
		model = Address
    	fields = ('pin','po','town','district','state','acno')

class VoterForm(forms.ModelForm):
	name = forms.CharField(max_length=50,help_text="Enter your name:")  # Field name made lowercase.
	age = forms.IntegerField(validators=[MinValueValidator(18)],help_text="Enter your age")  # Field name made lowercase.
	gender = forms.ChoiceField(label=u'sex', choices=[('Male','Male'),('Female','Female'),('Other','Other')], widget=forms.Select(), required=False,help_text="Enter your gender:")
	dob = forms.DateField()  # Field name made lowercase.
	emailid = forms.EmailField(max_length=100,help_text="Enter your emailid:")  # Field name made lowercase.
	phoneno = forms.IntegerField(help_text="Enter your phoneno:")  # Field name made lowercase.
	houseno = forms.IntegerField(help_text="Enter your houseno:")  # Field name made lowercase.
	streetno = forms.CharField(max_length=20,help_text="Enter your streetno:")  # Field name made lowercase.
	pin = forms.ModelChoiceField(queryset=Address.objects.all(),help_text="Select your pin code:")  # Field name made lowercase.
	town = forms.ModelChoiceField(queryset=Address.objects.all(),help_text="Select your town:")  # Field name made lowercase.
	caste = forms.ChoiceField(label='Caste',choices=[('ST','Scheduled Tribe'),('SC','Scheduled Caster'),('OBC','Other Backward Classes'),('GEN','General')],help_text="Enter your caste:")  # Field name made lowercase.
	#partno = forms.CharField(initial = 0,help_text="Part no")
	# def clean(self):
	# 	dob = self.cleaned_data['dob']
	# 	today = datetime.date.today()
	# 	if (dob.year + 18, dob.month, dob.day) > (today.year, today.month, today.day):
	# 		raise forms.ValidationError('Must be at least 18 years old to register')
	# 	return dob
	class Meta:
		model = Voter
		fields = ('name','age','gender','dob','emailid','phoneno','houseno','streetno','pin','town','caste')
		#exclude = ('voterid','doa','doi','picno','partno',)
class PartyForm(forms.ModelForm):
	partyname = forms.CharField(max_length=50, help_text = "Enter Party Name:")  # Field name made lowercase.
	symbol = forms.CharField(max_length = 100, help_text = "Enter Symbol")  # Field name made lowercase.
	type = forms.CharField(max_length=10, help_text = "Enter type")  # Field name made lowercase.
 	class Meta:
         model = Party
         fields = ('partyname','symbol','type')

class CandidateForm(forms.ModelForm):
	#candidateid = models.CharField(max_length=10, help_text = )  # Field name made lowercase.
	voterid = forms.ModelChoiceField(queryset=Voter.objects.all(),help_text = "Enter voterid:")  # Field name made lowercase.
	acno = forms.ModelChoiceField(queryset=Constituency.objects.all(),help_text = "Enter acno:")  # Field name made lowercase.
	type = forms.CharField(max_length=3, help_text = "Type of candidate ")  # Field name made lowercase.
	partyid = forms.ModelChoiceField(queryset=Party.objects.all(),help_text = "Enter partyid:")  # Field name made lowercase.
	class Meta:
		model = Candidate
		fields = ('voterid','acno','type','partyid')

	# def save(self, force_insert=False, force_update=False, commit=True):
	# 	m = Candidate
	# 	m.type = self.type
	# 	m.partyid = self.partyid
	# 	m.acno = self.acno
	# 	m.voterid = Voter.objects.get(voterid=self.voterid)

	# 	# do custom stuff
	# 	if commit:
	# 	    m.save()
	# 	return m
