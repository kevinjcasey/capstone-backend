from django.db import models

class Users(models.Model):
  user_name = models.CharField(max_length=100)
  password = models.CharField(max_length=32)
  high_score = models.IntegerField()

CATEGORY_CHOICES = (
  ('General Knowledge', 'GENERAL KNOWLEDGE')
  ('Entertainment: Books', 'ENTERTAINMENT: BOOKS')
  ('Entertainment: Film', 'ENTERTAINMENT: FILM')
  ('Entertainment: Music', 'ENTERTAINMENT: MUSIC')
  ('Entertainment: Musicals & Theatres', 'ENTERTAINMENT: MUSICALS & THEATRES')
  ('Entertainment: Television', 'ENTERTAINMENT: TELEVISION')
  ('Entertainment: Video Games', 'ENTERTAINMENT: VIDEO GAMES')
  ('Entertainment: Board Games', 'ENTERTAINMENT: BOARD GAMES')
  ('Science & Nature', 'SCIENCE & NATURE')
  ('Science: Computers', 'SCIENCE: COMPUTERS')
  ('Science: Mathematics', 'SCIENCE: MATHEMATICS')
  ('Mythology', 'MYTHOLOGY')
  ('Sports', 'SPORTS')
  ('Geography', 'GEOGRAPHY')
  ('History', 'HISTROY')
  ('Politics', 'POLITICS')
  ('Art', 'ART')
  ('Celebrities', 'CELEBRITIES')
  ('Animals', 'ANIMALS')
  ('Vehicles', 'VECHICLES')
  ('Entertainment: Comics', 'ENTERTAINMENT: COMICS')
  ('Science: Gadgets', 'SCIENCE: GADGETS')
  ('Entertainment: Japanese Anime and Manga', 'ENTERTAINMENT: JAPANESE ANIME & MANGA')
  ('Entertainment: Cartoon & Animations', 'ENTERTAINMENT: CARTOON & ANIMATIONS')
)

DIFFICULTY_CHOICES = (
  ('Easy', 'EASY')
  ('Medium', 'MEDIUM')
  ('Hard', 'HARD')
)

TYPE_CHOICES = (
  ('Multiple Choice', 'MULTILPLE CHOICE')
  ('True/False', 'TRUE/FALSE')
)

class Trivia(models.Model):
  category = models.CharField(max_length=100, choices=CATEGORY_CHOICES, default='General Knowledge')
  difficulty = models.CharField(max_length=6, choices=DIFFICULTY_CHOICES, default='Easy')
  questionType = models.CharField(max_length=32, choices=TYPE_CHOICES, default='Multiple Choice')
  question = models.CharField(max_length=100)
  answer = models.