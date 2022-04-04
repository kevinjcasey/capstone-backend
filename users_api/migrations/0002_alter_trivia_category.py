# Generated by Django 4.0.3 on 2022-04-04 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trivia',
            name='category',
            field=models.CharField(choices=[('General Knowledge', 'GENERAL KNOWLEDGE'), ('Entertainment: Books', 'ENTERTAINMENT: BOOKS'), ('Entertainment: Film', 'ENTERTAINMENT: FILM'), ('Entertainment: Music', 'ENTERTAINMENT: MUSIC'), ('Entertainment: Musicals & Theatres', 'ENTERTAINMENT: MUSICALS & THEATRES'), ('Entertainment: Television', 'ENTERTAINMENT: TELEVISION'), ('Entertainment: Video Games', 'ENTERTAINMENT: VIDEO GAMES'), ('Entertainment: Board Games', 'ENTERTAINMENT: BOARD GAMES'), ('Science & Nature', 'SCIENCE & NATURE'), ('Science: Computers', 'SCIENCE: COMPUTERS'), ('Science: Mathematics', 'SCIENCE: MATHEMATICS'), ('Mythology', 'MYTHOLOGY'), ('Sports', 'SPORTS'), ('Geography', 'GEOGRAPHY'), ('History', 'HISTORY'), ('Politics', 'POLITICS'), ('Art', 'ART'), ('Celebrities', 'CELEBRITIES'), ('Animals', 'ANIMALS'), ('Vehicles', 'VECHICLES'), ('Entertainment: Comics', 'ENTERTAINMENT: COMICS'), ('Science: Gadgets', 'SCIENCE: GADGETS'), ('Entertainment: Japanese Anime and Manga', 'ENTERTAINMENT: JAPANESE ANIME & MANGA'), ('Entertainment: Cartoon & Animations', 'ENTERTAINMENT: CARTOON & ANIMATIONS')], default='General Knowledge', max_length=100),
        ),
    ]
