from .models import TechTopic

def add_tech_topics_to_context(request):
    return {
        'tech_topics': TechTopic.objects.all(),
    }
