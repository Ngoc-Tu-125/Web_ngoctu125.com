from django.shortcuts import render, get_object_or_404
from .models import TechSharing

def home(request):
    return render(request, 'home.html')

def tech_sharing(request):
    tech_sharing_posts = TechSharing.objects.all().order_by('-date_published')
    return render(request, 'tech_sharing.html', {'tech_sharing_posts': tech_sharing_posts})

def tech_sharing_detail(request, slug):
    tech_sharing_post = get_object_or_404(TechSharing, slug=slug)
    return render(request, 'tech_sharing_post_content.html', {'tech_sharing_post': tech_sharing_post})