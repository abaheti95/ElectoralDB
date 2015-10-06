from django import forms
from electoraldbapp.models import Party
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import datetime
import html5.forms.widgets as html5_widgets

forms.DateInput.input_type="date"
forms.DateTimeInput.input_type="datetime-local" 

class PartyForm(forms.ModelForm):
 	class Meta:
         model = Party
         fields = ('partyname','symbol','type')

