from django import forms

from .models import Dash

class DashForm(forms.ModelForm):
    class Meta:
        model =  Dash
        fields  = [
            'title',
            'file',
        ]
