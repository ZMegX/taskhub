from django import forms
from .models import Request

class RequestForm(forms.ModelForm):
    scheduled_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Request
        fields = ['scheduled_date', 'message']