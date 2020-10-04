# Generated by Django 3.0.5 on 2020-05-09 07:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('Movie_id', models.IntegerField(primary_key=True, serialize=False)),
                ('Movie_Name', models.CharField(max_length=128, unique=True)),
                ('Movie_Genre', models.CharField(max_length=128)),
                ('Movie_Language', models.CharField(default='English', max_length=128)),
                ('Movie_Plot', models.TextField()),
                ('Movie_Year', models.IntegerField()),
                ('Movie_Rating', models.FloatField(default=0)),
                ('Movie_Imdb', models.URLField(default='')),
                ('Movie_Poster', models.URLField(default='')),
                ('Movie_Alt', models.CharField(default='', max_length=50)),
                ('Movie_Trailer', models.URLField(default='')),
                ('Movie_Price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Watch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=128)),
                ('movie_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.Movie')),
            ],
        ),
        migrations.CreateModel(
            name='Seen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=128)),
                ('movie_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.Movie')),
            ],
        ),
        migrations.CreateModel(
            name='Rent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(default='', max_length=128)),
                ('movie_id', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='movie.Movie')),
                ('user', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=128)),
                ('From_Email', models.EmailField(max_length=254)),
                ('Messages', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]