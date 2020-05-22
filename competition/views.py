from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from .forms import CompetitionForm
from .models import Competition

@login_required
def score_prediction(request):
    try:
        entry_form = Competition.objects.get(customer=request.user)
        form = CompetitionForm(instance=entry_form)
    except Competition.DoesNotExist:
        return redirect(score_prediction_new)
    
    if request.method == "POST":
        form = CompetitionForm(request.POST, instance=entry_form)
        if form.is_valid():
            temp = form.save(commit=False)
            temp.customer = request.user
            temp.save()
            return redirect('/accounts/profile/')

           
    return render(request, "competition.html", {'form': form})

def score_prediction_new(request):
    
    form = CompetitionForm()
    if request.method == "POST":
        form = CompetitionForm(request.POST)
        if form.is_valid():
            temp = form.save(commit=False)
            temp.customer = request.user
            temp.save()
            return redirect('/accounts/profile/')
        
    return render(request, "competition.html", {'form': form})

