# Generated by Django 5.0.4 on 2024-07-24 16:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_alter_category_options_blog'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='sluf',
            new_name='slug',
        ),
    ]
