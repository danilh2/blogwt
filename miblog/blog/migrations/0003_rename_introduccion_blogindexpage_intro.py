# Generated by Django 3.2.10 on 2022-01-11 09:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_rename_intro_blogindexpage_introduccion'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogindexpage',
            old_name='introduccion',
            new_name='intro',
        ),
    ]
