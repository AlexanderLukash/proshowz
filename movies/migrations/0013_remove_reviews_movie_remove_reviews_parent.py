# Generated by Django 4.0.5 on 2022-06-30 13:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0012_alter_movie_description_small'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reviews',
            name='movie',
        ),
        migrations.RemoveField(
            model_name='reviews',
            name='parent',
        ),
    ]
