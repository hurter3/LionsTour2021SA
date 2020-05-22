from django import forms
from .models import Competition

class CompetitionForm(forms.ModelForm):
    class Meta:
        model = Competition
        fields = [
        'sascore1', 'lionsscore1','sascore2', 'lionsscore2'
        ]