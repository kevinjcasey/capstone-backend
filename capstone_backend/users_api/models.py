from django.db import models

## Add favorite film option?

class Users(models.Model):
  user_name = models.CharField(max_length=100)
  password = models.CharField(max_length=32)
  high_score = models.IntegerField()