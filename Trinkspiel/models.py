from django.db import models

# Create your models here.

class game(models.Model):


class player(models.Model):
    name = models.CharField(max_length=100)
    sip = models.IntegerField
    shots = models.IntegerField
    # game = game
