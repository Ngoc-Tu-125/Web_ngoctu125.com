from django.contrib import admin
from .models import TechSharing, HomePageText, TechTopic, Tag


@admin.register(HomePageText)
class HomePageTextAdmin(admin.ModelAdmin):
    list_display = ('identifier', 'content')

@admin.register(TechTopic)
class TechTopicAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    prepopulated_fields = {"slug": ("title",)}

class TechSharingAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_published', 'topic', 'slug')
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Tag)
admin.site.register(TechSharing, TechSharingAdmin)