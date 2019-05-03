from django import forms


class Download(forms.Form):
    link = forms.CharField(label='Link', max_length = 100)
    email = forms.EmailField(label = 'Email', max_length = 100)
