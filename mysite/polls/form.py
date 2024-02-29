from django import forms 

from .models import Event

class e(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['event_name', 'description', 'start_date', 'location']



#update form
class eu(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['event_name', 'description', 'start_date', 'location']


