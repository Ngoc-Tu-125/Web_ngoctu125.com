from django.shortcuts import render, get_object_or_404
from .models import TechSharing, TechTopic, HomePageText
from django.http import JsonResponse
from django.template.loader import render_to_string

def home(request):
    home_texts = HomePageText.objects.all()
    # Convert texts to a dictionary for easy access in the template
    home_texts_dict = {text.identifier: text.content for text in home_texts}

    tech_topics = TechTopic.objects.all()  # Get all TechTopic instances
    return render(request, 'home.html', {'tech_topics': tech_topics, 'home_texts': home_texts_dict})

def tech_sharing(request, topic_slug=None):
    if topic_slug:
        topic = get_object_or_404(TechTopic, slug=topic_slug)
        tech_sharing_posts = TechSharing.objects.filter(topic=topic).order_by('-date_published')
    else:
        tech_sharing_posts = TechSharing.objects.all().order_by('-date_published')
    return render(request, 'tech_sharing.html', {'tech_sharing_posts': tech_sharing_posts, 'topic': topic if topic_slug else None})

def tech_sharing_detail(request, topic_slug, post_slug):
    topic = get_object_or_404(TechTopic, slug=topic_slug)
    tech_sharing_post = get_object_or_404(TechSharing, slug=post_slug, topic=topic)
    sections = tech_sharing_post.get_sections()
    content = render_to_string('tech_sharing_post_content.html', {'tech_sharing_post': tech_sharing_post})
    # Convert content to a string and sections to a list of dicts
    return JsonResponse({
        'content': content,
        'sections': sections
    })