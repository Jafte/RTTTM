from django.forms import ModelForm, TextInput, Textarea
from sound.models import Request


class RequestForm(ModelForm):
    class Meta:
        model = Request
        fields = ('title', 'description', 'url_to_source', 'text_source')
        widgets = {
            'title': TextInput(attrs={'class': 'uk-width-1-1'}),
            'description': Textarea(attrs={'class': 'uk-width-1-1', 'rows': 10}),
            'url_to_source': TextInput(attrs={'class': 'uk-width-1-1'}),
            'text_source': Textarea(attrs={'class': 'uk-width-1-1', 'rows': 5}),
        }
        labels = {
            'title': 'Что будем читать?',
            'description': 'Подробности',
            'url_to_source': 'Ссылка на оригинал',
            'text_source': 'Оригинал',
        }