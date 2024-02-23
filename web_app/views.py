from django.shortcuts import render, get_object_or_404
from .models import TechSharing
from django.http import JsonResponse
from django.template.loader import render_to_string

def home(request):
    return render(request, 'home.html')

def tech_sharing(request):
    tech_sharing_posts = TechSharing.objects.all().order_by('-date_published')
    return render(request, 'tech_sharing.html', {'tech_sharing_posts': tech_sharing_posts})

def tech_sharing_detail(request, slug):
    tech_sharing_post = get_object_or_404(TechSharing, slug=slug)
    sections = tech_sharing_post.get_sections()
    content = render_to_string('tech_sharing_post_content.html', {'tech_sharing_post': tech_sharing_post})
    # Convert content to a string and sections to a list of dicts
    return JsonResponse({
        'content': content,
        'sections': sections
    })