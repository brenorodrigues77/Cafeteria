from django import forms

class coffeForm(forms.Form):
    title = forms.CharField()
    description = forms.CharField(max_length=200,)
    value = forms.FloatField()
    photo = forms.ImageField()