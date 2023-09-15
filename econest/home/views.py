from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, "home.html")

def login_view(request):
    return render(request, "login.html")

def search(request):
    return render(request, "search.html")

def maps(request):
    return render(request, "maps.html")

