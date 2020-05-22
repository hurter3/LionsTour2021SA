from django import forms
from .models import Competition

class CompetitionForm(forms.ModelForm):
    class Meta:
        model = Competition
        fields = [
        'sascore1', 'lionsscore1','sascore2', 'lionsscore2',
        'sascore3', 'lionsscore3','sascore4', 'lionsscore4',
        'sascore5', 'lionsscore5','sascore6', 'lionsscore6',
        'sascore7', 'lionsscore7','sascore8', 'lionsscore8',
        'points_accrued'
        ]