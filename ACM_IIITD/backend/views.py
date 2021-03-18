from django.shortcuts import render
from .models import image
def index(request):
    return render(request, "index.html")

def members(request):
    return render(request, "members.html")

