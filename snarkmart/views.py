"""
Mainly just used for the home page
"""
from django.shortcuts import render

def index(request):
    return render(request, "index.html")