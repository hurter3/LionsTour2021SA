from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import CompetitionForm
from .models import Competition

@login_required
def score_prediction(request):  
    if request.method == "POST":
        form = CompetitionForm(request.POST)
        if form.is_valid():
            temp = form.save(commit=False)
            temp.customer = request.user
            temp.save()
    else:
        form = CompetitionForm(request.GET)
    context = {
    'form' : form
    }
    return render(request, "competition.html",context)
