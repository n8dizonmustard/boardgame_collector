from django.db import models
from django.urls import reverse

# Create your models here.
class Store(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('stores_detail', kwargs={'pk': self.id})

class Boardgame(models.Model):
    name = models.CharField(max_length=100)
    players = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    release = models.IntegerField()
    stores = models.ManyToManyField(Store)

    def get_absolute_url(self):
        return reverse('detail', kwargs={'boardgame_id': self.id})
        # detail is defined from Model (name="detail")
        # kwargs='boardgame_id' is how we've written our boardgames' ids
        # self.id calls on Boardgame Model and its id

RATING = ( # this is a tuple (immutable)
    ('1/5', 'Boring'),
    ('2/5', 'Okay'),
    ('3/5', 'Fun'),
    ('4/5', 'Great'),
    ('5/5', 'Awesome'),
)

# New model > save it with makemigrations
class Review(models.Model):
    content = models.TextField('Review', max_length=250)
    stars = models.CharField(
        max_length=3,
        choices=RATING,
        default=RATING[0][0]
    )

    # This means if a Boardgame is deleted, also delete all its reviews
    boardgame = models.ForeignKey(Boardgame, on_delete=models.CASCADE)

    def __str__(self):
        # Nice method for obtaining the friendly value of a Field.choice (RATING)
        return f"{self.get_stars_display()} on {self.content}" #<<<NO IDEA HOW THIS WILL LOOK