from django import forms

class PostCreateForm(forms.Form):
    image = forms.FileField(required= False)
    title = forms.CharField(max_length=32, min_length=3)
    rate = forms.FloatField(max_value=5)
    description = forms.CharField(widget=forms.Textarea())