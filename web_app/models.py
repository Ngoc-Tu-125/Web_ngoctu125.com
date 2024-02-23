from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from django.utils.text import slugify

class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class TechSharing(models.Model):
    title = models.CharField(max_length=255)
    date_published = models.DateTimeField(auto_now_add=True)
    full_content = CKEditor5Field('Content', config_name='extends')
    slug = models.SlugField(max_length=255, unique=True)  # Make slug not editable from the admin
    tags = models.ManyToManyField(Tag, related_name='tech_sharing')

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
        # This method needs to parse the full_content and extract headers
        # Placeholder for BeautifulSoup parsing or similar
        pass
