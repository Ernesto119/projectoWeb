from django.db import models
from datetime import date
from django_ckeditor_5.fields import CKEditor5Field
from django.utils.text import slugify


class Post(models.Model):
    title = models.CharField(max_length=100, null=False)
    image = models.ImageField(null=True, blank=True, upload_to="blog/images")
    publish = CKEditor5Field(blank=True, config_name="extends")
    date = models.DateField(default=date.today)
    slug = models.SlugField(max_length=255, unique=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title + "-" + self.date)
        super().save(*args, **kwargs)
