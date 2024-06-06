from django import forms

class inputforms(forms.Form):
    word3 = forms.CharField(label='Enter a 3 Letter word:')
    #word4 = forms.CharField(max_length=4, label='Enter a 4 Letter word:')