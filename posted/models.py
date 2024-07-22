from django.db import models
from datetime import date
from django_ckeditor_5.fields import CKEditor5Field
from django.utils.text import slugify
from PIL import Image as PilImage

class Post(models.Model):
    title = models.CharField(max_length=100, null=False)
    image = models.ImageField(null=True, blank=True, upload_to="blog/images")
    publish = CKEditor5Field(blank=True, config_name="extends")
    date = models.DateField(default=date.today)
    slug = models.SlugField(max_length=255, unique=True, null=True, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title + "-" + str(self.date))
        super().save(*args, **kwargs)
        
        if self.image:
            img = PilImage.open(self.image.path)
            output_size = (800, 800)  # Ajusta el tamaño según tus necesidades
            img.thumbnail(output_size)
            img.save(self.image.path)