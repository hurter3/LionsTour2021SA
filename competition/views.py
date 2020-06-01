from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CompetitionForm
from .models import Competition


def competition_rules_view(request):
    return render(request, "competition-rules.html")

def competition_terms_view(request):
    return render(request, "competition-terms.html")

@login_required
def score_prediction(request):
    try:
        entry_form = Competition.objects.get(customer=request.user)
        points = entry_form.points_accrued
        form = CompetitionForm(instance=entry_form)
    except Competition.DoesNotExist:
        return redirect(score_prediction_new)
    
    if request.method == "POST":
        form = CompetitionForm(request.POST, instance=entry_form)
        if form.is_valid():
            temp = form.save(commit=False)
            temp.customer = request.user
            temp.save()
            messages.success(request, f'You have successfuly updated your score predictions. GOOD LUCK!')
            return redirect('/')

           
    return render(request, "competition.html", {'form': form, 'points':points})

def score_prediction_new(request):
    
    form = CompetitionForm()
    points = 0
    if request.method == "POST":
        form = CompetitionForm(request.POST)
        if form.is_valid():
            temp = form.save(commit=False)
            temp.customer = request.user
            temp.save()
            messages.success(request, f'You have successfuly submitted your score predictions. GOOD LUCK!')
            return redirect('/')
        
    return render(request, "competition.html", {'form': form,'points':points})

