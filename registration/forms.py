from django import forms

class FeedbackForm(forms.Form):
    name = forms.CharField(max_length=100,)
    message = forms.CharField(widget=forms.Textarea)
