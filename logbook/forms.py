from django import forms
from .models import Dive

class DiveForm(forms.ModelForm):
    class Meta:
        model = Dive
        fields = ('diver', 'location', 'date', 'start_time', 'duration', 'max_depth', 'buddy_name', 'log_text')
