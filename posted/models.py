from django.db import models
import datetime
from ckeditor.fields import RichTextField

class Post(models.Model):
    title = models.CharField(max_length=100, null=False)
    image = models.ImageField(null=True,blank=True,upload_to='media')
    publish = RichTextField(blank=True)
    date = models.DateField(datetime.date.today)

