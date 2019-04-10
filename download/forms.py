from django import forms


class download(forms.Form):
    link = forms.CharField(label='link', max_length = 100)
