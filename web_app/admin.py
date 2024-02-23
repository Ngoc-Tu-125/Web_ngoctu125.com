from django.contrib import admin
from .models import TechSharing, Tag

class TechSharingAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_published', 'slug')
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Tag)
admin.site.register(TechSharing, TechSharingAdmin)