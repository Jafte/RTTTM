from django import forms
from django.utils.translation import ugettext_lazy as _


class ProfileForm(forms.Form):
    name = forms.CharField(label=_('Name'), max_length=100, required=False)
    about = forms.CharField(label=_('About'), widget=forms.Textarea, required=False)
    photo = forms.FileField(label=_('Photo'), required=False)
