# Generated by Django 3.2 on 2023-09-24 11:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_rename_slug_category_cat_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='cat_slug',
            new_name='slug',
        ),
    ]
