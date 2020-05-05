from django.shortcuts import render

def prediction_scores(request):
    return render(request, "competition.html")