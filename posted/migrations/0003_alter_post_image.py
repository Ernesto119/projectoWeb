# Generated by Django 5.0.4 on 2024-04-22 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posted', '0002_alter_post_date_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='photos'),
        ),
    ]