from django.shortcuts import render

def home_view(request):
    return render(request, "index.html")

def history_view(request):
    return render(request, "history.html", {"home": "history"})

def photos_view(request):
    return render(request, "photos.html")

def tickets_view(request):
    return render(request, "tickets.html")