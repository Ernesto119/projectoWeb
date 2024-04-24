from django.db import models
import datetime
from django_ckeditor_5.fields import CKEditor5Field


class Post(models.Model):
    title = models.CharField(max_length=100, null=False)
    image = models.ImageField(null=True, blank=True, upload_to="media")
    publish = CKEditor5Field(blank=True, config_name="extends")
    date = models.DateField(datetime.date.today)
