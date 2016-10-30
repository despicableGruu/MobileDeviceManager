from django import forms

class contactForm(forms.Form):
    name = forms.CharField(required = False, max_length = 100, help_text = '100 characters max')
    email = forms.EmailField()
    comment = forms.CharField(widget = forms.Textarea)