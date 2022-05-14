# Generated by Django 3.1.2 on 2022-05-13 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0002_remove_phone_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='phone',
            name='slug',
            field=models.SlugField(default=2, unique=True),
            preserve_default=False,
        ),
    ]