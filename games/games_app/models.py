from django.db import models
from users.models import Publisher

from django.db.models import signals


# Create your models here.

class CategoryManager(models.Manager):
    def get_total_objects(self):
        return self.all().count()

    def get_all_objects(self):
        return self.all()


class Category(models.Model):
    title_category = models.CharField(max_length=20)

    objects = CategoryManager()

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.title_category


class GameManager(models.Manager):
    def get_all(self):
        return self.all()

    def name_ptn(self, ptn):
        return self.filter(name__contains=ptn)


class Game(models.Model):
    name = models.CharField(max_length=50, unique=True)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    price = models.IntegerField(verbose_name='price')
    image = models.ImageField(upload_to='games_app/')
    file = models.FileField(upload_to='documents/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    objects = GameManager()


def create_Category(sender, instance, created, **kwargs):
    print("Saved Category is called")


signals.post_save.connect(receiver=create_Category, sender=Category)
