from django.shortcuts import render

def home_view(request):
    return render(request, "home.html")

def history_view(request):
    return render(request, "history.html", {"home": "history"})

def photos_view(request):
    return render(request, "photos.html", {"home": "photos"})

def fixtures_view(request):
    return render(request, "fixtures.html", {"home": "fixtures"})

def tickets_view(request):
    return render(request, "tickets.html", {"home": "tickets"})

def contact_view(request):
    return render(request, "contact.html", {"home": "contact"})