# Generated by Django 5.0.6 on 2024-05-10 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posted', '0003_alter_post_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='blog/images'),
        ),
    ]