from django.db import models
from django.core.validators import MaxValueValidator
from users.models import Customer
from games_app.models import Game
# Create your models here.
class OrderManager(models.Manager):
    def get_total(self):
        return self.all().count()

    def get_all(self):
        return self.all()

class Order(models.Model):
    username = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(validators = [MaxValueValidator(101)])
    game_name = models.ForeignKey(Game, on_delete=models.CASCADE)

    objects = OrderManager()