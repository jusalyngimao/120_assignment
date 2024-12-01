# sms/forms.py
from django import forms

class SmsForm(forms.Form):
    phone_number = forms.CharField(max_length=15, label="Phone Number")
    message = forms.CharField(widget=forms.Textarea, label="Message")
