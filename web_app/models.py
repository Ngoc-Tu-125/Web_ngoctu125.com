from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.text import slugify
from bs4 import BeautifulSoup
from django.conf import settings


class HomePageText(models.Model):
    IDENTIFIER_CHOICES = [
        ('home_intro', 'Home Introduction'),
        ('home_about', 'Home About'),
        ('home_tech_sharing', 'Home Tech Sharing'),
        ('home_github_repo', 'Home Github Repository'),
    ]

    identifier = models.CharField(max_length=100, choices=IDENTIFIER_CHOICES, unique=True)
    content = models.TextField()

    def __str__(self):
        return self.get_identifier_display()

class Contacts(models.Model):
    IDENTIFIER_CHOICES = [
        ('contacts_facebook', 'Facebook'),
        ('contacts_instagram', 'Instagram'),
        ('contacts_linkedln', 'Linkedln'),
    ]

    identifier = models.CharField(max_length=100, choices=IDENTIFIER_CHOICES, unique=True)
    link = models.TextField()

    def __str__(self):
        return self.get_identifier_display()


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class TechTopic(models.Model):
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    slug = models.SlugField(max_length=255, unique=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.pk:  # Only set the slug when the object is first created
            self.slug = slugify(self.title)
        super(TechTopic, self).save(*args, **kwargs)

class TechSharing(models.Model):
    title = models.CharField(max_length=255)
    date_published = models.DateTimeField(auto_now_add=True)
    full_content = RichTextUploadingField(default="Tech Sharing content")
    slug = models.SlugField(max_length=255, unique=True)  # Make slug not editable from the admin
    tags = models.ManyToManyField(Tag, related_name='tech_sharing')
    is_hidden = models.BooleanField(default=False)
    topic = models.ForeignKey(TechTopic, on_delete=models.CASCADE, related_name='tech_sharings')  # ForeignKey added

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # Only set the slug when the object is first created
        if not self.pk:  # Checking if the object is new
            self.slug = slugify(self.title)
        super(TechSharing, self).save(*args, **kwargs)

    def display_tags(self):
        """Returns a string of tags prefixed with '#' and joined by spaces."""
        return ' '.join([f'#{tag.name}' for tag in self.tags.all()])

    def get_sections(self):
        """Parse the full_content and extract H2 and H3 headings."""
        soup = BeautifulSoup(self.full_content, "html.parser")
        headings = soup.find_all(['h2', 'h3'])
        sections = []
        for idx, heading in enumerate(headings):
            id_base = slugify(heading.text)[:30]  # Shorten and slugify the text to create a base for the ID
            unique_id = f"{id_base}-{idx}"  # Append the index to ensure uniqueness
            sections.append({'tag': heading.name, 'text': heading.text.strip(), 'id': unique_id})
        return sections



# About me
class SingletonModel(models.Model):
    class Meta:
        abstract = True  # Specifies that this model is an abstract base class

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)
        # Delete any extra instances
        self.__class__.objects.exclude(pk=self.pk).delete()

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj

class Summary(SingletonModel):
    summary = models.TextField()

    def __str__(self):
        return self.summary

class Skills(models.Model):
    skill_text = models.TextField()

    def __str__(self):
        return self.skill_text

class TechSkill(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class WorkExperience(models.Model):
    job_position = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    description = models.TextField()
    skills = models.ManyToManyField(TechSkill)
    start_time = models.CharField(max_length=20)
    end_time = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.job_position} at {self.company_name}"

class PersonalProject(models.Model):
    project_name = models.CharField(max_length=255)
    description = models.TextField()
    skills = models.ManyToManyField(TechSkill)
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.project_name

class Education(models.Model):
    university_name = models.CharField(max_length=255)
    degree = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.degree} from {self.university_name}"

class PersonalContacts(SingletonModel):
    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    address = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"{self.phone}, {self.email}"

class Greeting(SingletonModel):
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    greeting = models.CharField(max_length=255, blank=True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.greeting