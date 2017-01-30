from django import forms

class ReviewForm(forms.Form):
    """TODO: Docstring"""
    title = forms.CharField(required=False, max_length=100, help_text='100 characters max')
    body = forms.CharField(widget=forms.Textarea)
    rating = forms.IntegerField()
