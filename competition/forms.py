from django import forms
from .models import Competition

class CompetitionForm(forms.ModelForm):
    class Meta:
        model = Competition
                      
        fields = [
        'sascore1', 'lionsscore1', 'firstpoints1',
        'sascore2', 'lionsscore2', 'firstpoints2',
        'sascore3', 'lionsscore3', 'firstpoints3',
        'sascore4', 'lionsscore4', 'firstpoints4',
        'sascore5', 'lionsscore5', 'firstpoints5',
        'sascore6', 'lionsscore6', 'firstpoints6',
        'sascore7', 'lionsscore7', 'firstpoints7',
        'sascore8', 'lionsscore8', 'firstpoints8'
        ]