from django import forms
from .models import PhotoContestEntry

class PhotoContestForm(forms.ModelForm):
    """
    Form for the photo contest
    """

    #  Fields to be displayed from the PhotoContestEntry model from models.py
    class Meta:
        model = PhotoContestEntry
        fields = ['first_name', 'last_name', 'email', 'photo']
