from django import forms
from django.utils.translation import ugettext_lazy as _


class ProfileForm(forms.Form):
    name = forms.CharField(
        label=_('Name'),
        widget=forms.TextInput(attrs={'class': 'uk-width-1-1'}),
        max_length=100,
        required=False
    )
    about = forms.CharField(
        label=_('About'),
        widget=forms.Textarea(attrs={'class': 'uk-width-1-1', 'rows': 10}),
        required=False
    )
    photo = forms.FileField(
        label=_('Photo'),
        required=False
    )


class WantToReadForm(forms.Form):
    message = forms.CharField(
        label=_('Message'),
        widget=forms.Textarea(attrs={'class': 'uk-width-1-1', 'rows': 10})
    )
