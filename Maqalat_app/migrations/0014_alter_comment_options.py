# Generated by Django 4.0.5 on 2022-07-22 09:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Maqalat_app', '0013_alter_comment_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-created']},
        ),
    ]
