from django import forms

class Calcform(forms.Form):

    expression = forms.CharField(max_length=200)
    result = forms.CharField(max_length=200,required=False,disabled=True)
    

