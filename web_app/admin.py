from django.contrib import admin
from .models import (TechSharing, HomePageText, TechTopic, Tag, Contacts,
                     Greeting, Summary, TechSkill, WorkExperience,
                     PersonalProject, Education, PersonalContacts, Skills
)


@admin.register(HomePageText)
class HomePageTextAdmin(admin.ModelAdmin):
    list_display = ('identifier', 'content')

@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    list_display = ('identifier', 'link')

@admin.register(TechTopic)
class TechTopicAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    prepopulated_fields = {"slug": ("title",)}

class TechSharingAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_published', 'topic', 'slug')
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ('topic',)


admin.site.register(Tag)
admin.site.register(TechSharing, TechSharingAdmin)

# About
@admin.register(Summary)
class SummaryAdmin(admin.ModelAdmin):
    list_display = ('summary',)

@admin.register(Skills)
class SkillsAdmin(admin.ModelAdmin):
    list_display = ('skill_text',)

@admin.register(TechSkill)
class TechSkillAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(WorkExperience)
class WorkExperienceAdmin(admin.ModelAdmin):
    list_display = ('job_position', 'company_name', 'start_time', 'end_time')
    filter_horizontal = ('skills',)

@admin.register(PersonalProject)
class PersonalProjectAdmin(admin.ModelAdmin):
    list_display = ('project_name',)
    filter_horizontal = ('skills',)

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('university_name', 'degree')

@admin.register(PersonalContacts)
class PersonalContactsAdmin(admin.ModelAdmin):
    list_display = ('phone', 'email', 'address')

@admin.register(Greeting)
class GreetingAdmin(admin.ModelAdmin):
    list_display = ('greeting', 'bio')
