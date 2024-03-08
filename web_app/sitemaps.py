# sitemaps.py

from django.contrib import sitemaps
from django.urls import reverse
from .models import (TechSharing, TechTopic, TechSkill)

class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.7
    changefreq = 'daily'

    def items(self):
        return ['home', 'about', 'tech-sharing']

    def location(self, item):
        return reverse(item)

class TechSharingSitemap(sitemaps.Sitemap):
    changefreq = "daily"
    priority = 0.8

    def items(self):
        return TechSharing.objects.exclude(is_hidden=True)

    def lastmod(self, obj):
        return obj.date_published

class TechTopicSitemap(sitemaps.Sitemap):
    changefreq = "daily"
    priority = 0.8

    def items(self):
        return TechTopic.objects.all()

class TechSkillSitemap(sitemaps.Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return TechSkill.objects.all()
