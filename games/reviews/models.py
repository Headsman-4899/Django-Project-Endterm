from django.db import models
from django.core.validators import MaxValueValidator, MinLengthValidator
from users.models import Customer
from games_app.models import Game
# Create your models here.
class ReviewManager(models.Manager):
    def get_reviews_by_game(self, game_name):
        return self.filter(to_game__exact=game_name)
class Review(models.Model):
    title = models.CharField(max_length=50)
    comment = models.CharField(max_length=400)
    rating = models.PositiveIntegerField(validators=[MinLengthValidator(1), MaxValueValidator(5)])
    reviewer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    to_game = models.ForeignKey(Game, on_delete=models.CASCADE)

    objects = ReviewManager()