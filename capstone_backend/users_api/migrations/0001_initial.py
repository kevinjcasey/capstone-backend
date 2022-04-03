# Generated by Django 4.0.3 on 2022-04-03 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trivia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('General Knowledge', 'GENERAL KNOWLEDGE'), ('Entertainment: Books', 'ENTERTAINMENT: BOOKS'), ('Entertainment: Film', 'ENTERTAINMENT: FILM'), ('Entertainment: Music', 'ENTERTAINMENT: MUSIC'), ('Entertainment: Musicals & Theatres', 'ENTERTAINMENT: MUSICALS & THEATRES'), ('Entertainment: Television', 'ENTERTAINMENT: TELEVISION'), ('Entertainment: Video Games', 'ENTERTAINMENT: VIDEO GAMES'), ('Entertainment: Board Games', 'ENTERTAINMENT: BOARD GAMES'), ('Science & Nature', 'SCIENCE & NATURE'), ('Science: Computers', 'SCIENCE: COMPUTERS'), ('Science: Mathematics', 'SCIENCE: MATHEMATICS'), ('Mythology', 'MYTHOLOGY'), ('Sports', 'SPORTS'), ('Geography', 'GEOGRAPHY'), ('History', 'HISTROY'), ('Politics', 'POLITICS'), ('Art', 'ART'), ('Celebrities', 'CELEBRITIES'), ('Animals', 'ANIMALS'), ('Vehicles', 'VECHICLES'), ('Entertainment: Comics', 'ENTERTAINMENT: COMICS'), ('Science: Gadgets', 'SCIENCE: GADGETS'), ('Entertainment: Japanese Anime and Manga', 'ENTERTAINMENT: JAPANESE ANIME & MANGA'), ('Entertainment: Cartoon & Animations', 'ENTERTAINMENT: CARTOON & ANIMATIONS')], default='General Knowledge', max_length=100)),
                ('difficulty', models.CharField(choices=[('Easy', 'EASY'), ('Medium', 'MEDIUM'), ('Hard', 'HARD')], default='Easy', max_length=6)),
                ('questionType', models.CharField(choices=[('Multiple Choice', 'MULTILPLE CHOICE'), ('True/False', 'TRUE/FALSE')], default='Multiple Choice', max_length=32)),
                ('question', models.CharField(max_length=1000)),
                ('correct_answer', models.CharField(max_length=255)),
                ('incorrect_answer_one', models.CharField(max_length=255)),
                ('incorrect_answer_two', models.CharField(max_length=255)),
                ('incorrect_answer_three', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=32)),
                ('high_score', models.IntegerField()),
            ],
        ),
    ]
