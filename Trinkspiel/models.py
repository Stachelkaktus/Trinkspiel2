from django.db import models

# Create your models here.

class game(models.Model):
    difficulty = models.IntegerField = 1


class player(models.Model):
    name = models.CharField(max_length=100)
    sip = models.IntegerField
    shots = models.IntegerField
    # game = game

class task(models.Model):
    target = player
    task = models.CharField(max_length=500)