# Generated by Django 5.0.4 on 2024-04-24 01:57

import django_ckeditor_5.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posted', '0004_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publish',
            field=django_ckeditor_5.fields.CKEditor5Field(blank=True),
        ),
    ]