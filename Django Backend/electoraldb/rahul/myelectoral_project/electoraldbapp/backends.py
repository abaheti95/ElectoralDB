from django.conf import settings
from django.contrib.auth.models import check_password
from electoraldbapp.models import Party,Candidate

class PartyidAuthBackend(object):
    """
    A custom authentication backend. Allows users to log in using their email address.
    """

    def authenticate(self, partyid=None, password=None):
        """
        Authentication method
        """
        try:
            if partyid[0]=='P':
                user = Party.objects.get(partyid=partyid)
                if user.check_password(password):
                    return user
            elif partyid[0]=='C':
                user = Candidate.objects.get(candidateid=partyid)
                if user.check_password(password):
                    return user
        except Party.DoesNotExist,Candidate.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            if user_id[0]=='P':
                user = Party.objects.get(partyid=user_id)
            elif user_id[0]=='C':
                user = Candidate.objects.get(candidateid=user_id)
            if user.is_active:
                return user
            return None
        except Party.DoesNotExist, Candidate.DoesNotExist:
            return None
