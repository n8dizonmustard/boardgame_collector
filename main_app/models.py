from django.db import models
from django.urls import reverse

# Create your models here.
class Boardgame(models.Model):
    name = models.CharField(max_length=100)
    players = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    release = models.IntegerField()

    def get_absolute_url(self):
        return reverse('detail', kwargs={'boardgame_id': self.id})
        # detail is defined from Model (name="detail")
        # kwargs='cat_id' is how we've written our cats' ids
        # self.id calls on Cat Model and its id