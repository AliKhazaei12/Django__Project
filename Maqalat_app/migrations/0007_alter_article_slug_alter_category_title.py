# Generated by Django 4.0.5 on 2022-07-14 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Maqalat_app', '0006_alter_article_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(unique=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
