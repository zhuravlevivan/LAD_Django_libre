# Generated by Django 4.2.7 on 2023-11-28 18:45

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('libre_authors', '0003_alter_libreauthors_options_libreauthors_slug_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libreauthors',
            name='slug',
            field=models.SlugField(max_length=255, unique=True),
        ),
    ]
