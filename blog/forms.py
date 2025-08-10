from django import forms
from blog.models import PhotoContestEntry

class PhotoContestForm(forms.ModelForm):
    class Meta:
        model = PhotoContestEntry
        fields = ['first_name', 'last_name', 'email', 'photo']