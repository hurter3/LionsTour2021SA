from django import forms
from .models import Competition

class CompetitionForm(forms.ModelForm):
    class Meta:
        model = Competition

        labels = {
        "sascore1": "SA Score","sascore2": "SA Score","sascore3": "SA Score","sascore4": "SA Score",
        "sascore5": "SA Score","sascore6": "SA Score","sascore7": "SA Score","sascore8": "SA Score",
        "lionsscore1": "Lion's Score" ,"lionsscore2": "Lion's Score" ,"lionsscore3": "Lion's Score", 
        "lionsscore4": "Lion's Score" ,"lionsscore5": "Lion's Score" ,"lionsscore6": "Lion's Score",
        "lionsscore7": "Lion's Score" ,"lionsscore8": "Lion's Score", 
        "firstpoints1" : "First Points Scored", "firstpoints2" : "First Points Scored",
        "firstpoints3" : "First Points Scored","firstpoints4" : "First Points Scored",
        "firstpoints5" : "First Points Scored","firstpoints6" : "First Points Scored",
        "firstpoints7" : "First Points Scored","firstpoints8" : "First Points Scored"
    }
       

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