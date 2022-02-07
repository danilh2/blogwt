# Generated by Django 3.2.10 on 2022-02-02 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peliculas', '0003_genre'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pelicula',
            options={'verbose_name': 'Película', 'verbose_name_plural': 'Películas'},
        ),
        migrations.AddField(
            model_name='pelicula',
            name='generos',
            field=models.ManyToManyField(to='peliculas.Genre'),
        ),
        migrations.AddField(
            model_name='pelicula',
            name='slug',
            field=models.SlugField(blank=True),
        ),
    ]
