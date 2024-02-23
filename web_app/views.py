from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def tech_sharing(request):
    return render(request, 'tech_sharing.html')