from django import forms

class SevensegForm(forms.Form):
    number = forms.RegexField(label='Number', regex=r"^\s*\d+\s*$")