# Generated by Django 4.0.5 on 2022-07-14 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Maqalat_app', '0009_alter_article_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
