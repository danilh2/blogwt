# Generated by Django 3.2.10 on 2022-01-11 09:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogindexpage',
            old_name='intro',
            new_name='introduccion',
        ),
    ]
