"""
URL configuration for web_manage project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from web_app import views
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from web_app.sitemaps import StaticViewSitemap, TechSharingSitemap, TechTopicSitemap, TechSkillSitemap

sitemaps = {
    'static': StaticViewSitemap,
    'tech_sharing': TechSharingSitemap,
    'tech_topic': TechTopicSitemap,
    'tech_skills': TechSkillSitemap,
}


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    # path('tech-sharing/', views.tech_sharing, name='tech_sharing'),
    path('tech-sharing/topic/<slug:topic_slug>/', views.tech_sharing, name='tech_sharing_by_topic'),
    path('tech-sharing/topic/<slug:topic_slug>/<slug:post_slug>/', views.tech_sharing_detail, name='tech_sharing_detail'),

    path('contacts/', views.contacts, name='contacts'),
    path('about/', views.about_me, name='about_me'),

    path('ckeditor/', include('ckeditor_uploader.urls')),

    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
