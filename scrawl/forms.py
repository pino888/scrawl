from django import forms
from .models import Scrawl


class ScrawlForm(forms.ModelForm):
    body = forms.CharField(required=True, widget=forms.widgets.Textarea(
            attrs={
                'placeholder': 'Scrawl something...',
                'class': '#',
            }
        ),
        label='',)

    class Meta:
        model = Scrawl
        exclude = ('user', 'quills', 'saved_by', 'quilled_by', 'type')
