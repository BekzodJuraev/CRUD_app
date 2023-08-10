from .models import CRUD
from django import forms

class MakeForm(forms.ModelForm):
    class Meta:
        model=CRUD
        fields=['user','text']


