from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.text import slugify
from bs4 import BeautifulSoup


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class TechSharing(models.Model):
    title = models.CharField(max_length=255)
    date_published = models.DateTimeField(auto_now_add=True)
    full_content = RichTextUploadingField(default="Tech Sharing content")
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
        """Parse the full_content and extract H2 and H3 headings."""
        soup = BeautifulSoup(self.full_content, "html.parser")
        headings = soup.find_all(['h2', 'h3'])
        sections = []
        for idx, heading in enumerate(headings):
            id_base = slugify(heading.text)[:30]  # Shorten and slugify the text to create a base for the ID
            unique_id = f"{id_base}-{idx}"  # Append the index to ensure uniqueness
            sections.append({'tag': heading.name, 'text': heading.text.strip(), 'id': unique_id})
        return sections

