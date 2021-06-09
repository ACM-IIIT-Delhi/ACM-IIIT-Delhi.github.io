from django.shortcuts import render
def index(request):
    return render(request, "index.html")

def members(request):
    return render(request, "members.html")

