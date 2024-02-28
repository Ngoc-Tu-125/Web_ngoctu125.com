from django.shortcuts import render, get_object_or_404
from .models import TechSharing, TechTopic, HomePageText, Contacts
from django.http import JsonResponse
from django.template.loader import render_to_string
import requests

def home(request):
    home_texts = HomePageText.objects.all()
    # Convert texts to a dictionary for easy access in the template
    home_texts_dict = {text.identifier: text.content for text in home_texts}

    contacts = Contacts.objects.all()
    # Convert texts to a dictionary for easy access in the template
    contacts_dict = {text.identifier: text.link for text in contacts}

    # Get tech topics
    tech_topics = TechTopic.objects.all()  # Get all TechTopic instances

    # Get repo in github
    response = requests.get('https://api.github.com/users/Ngoc-Tu-125/repos')
    repos = response.json()

    # Context
    context = {
        'tech_topics': tech_topics,
        'home_texts': home_texts_dict,
        'github_repos': repos,
        'contacts': contacts_dict,
    }

    return render(request, 'home.html', context)

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

def contacts(request):
    contacts = Contacts.objects.all()
    # Convert texts to a dictionary for easy access in the template
    contacts_dict = {text.identifier: text.link for text in contacts}
    return render(request, 'contacts.html', {'contacts': contacts_dict})