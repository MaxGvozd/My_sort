from django import forms
from .models import Execution


class InputForm(forms.Form):
    method = forms.ChoiceField(choices=Execution.METHODS)
    file = forms.FileField()
