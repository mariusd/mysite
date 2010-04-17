from django import forms

class WebstatForm(forms.Form):
    url = forms.URLField(label='Web site')