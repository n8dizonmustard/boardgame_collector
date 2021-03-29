from django.db import models

# Create your models here.
class Boardgame(models.Model):
    name = models.CharField(max_length=100)
    players = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    release = models.IntegerField()


# class Boardgame:  # Note that parens are optional if not inheriting from another class
#   def __init__(self, name, players, description, release):
#     self.name = name
#     self.players = players
#     self.description = description
#     self.release = release
# boardgames = [
#   Boardgame('Catan', '3-4', 'Build the best settlement on the island of Catan.', 1995),
#   Boardgame('Journeys in Middle Earth', '1-5', 'Play as one of many heroes of Middle Earth through a 12-15 chapter campaign.', 2019),
#   Boardgame('Secret Hitler', '5-10', 'Hidden identity, social deduction party game.', 2016)
# ]