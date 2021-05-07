from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

from django.db.models import signals


# Create your models here.
class BaseUserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    contact = PhoneNumberField(unique=True)
    date = models.DateField(verbose_name='Date of birth')

    class Meta:
        abstract = True


class PublisherManager(models.Manager):
    def customers(self):
        return self.all()

    def customer_by_ptn(self, ptn):
        return self.filter(firstname__contains=ptn)

    def customer_birth_date(self, year):
        return self.filter(date__year=year)


class Publisher(BaseUserProfile):
    objects = PublisherManager()

    def __str__(self):
        return f'{self.firstname} {self.lastname}'


class CustomerManager(models.Manager):
    def customers(self):
        return self.all()

    def customer_by_ptn(self, ptn):
        return self.filter(firstname__contains=ptn)

    def customer_birth_date(self, year):
        return self.filter(date__year=year)


class Customer(BaseUserProfile):
    card_number = models.CharField(max_length=40)

    objects = CustomerManager()

    def __str__(self):
        return f'{self.firstname} {self.lastname}'


def create_Customer(sender, instance, created, **kwargs):
    print("Saved Customer is called")


signals.post_save.connect(receiver=create_Customer, sender=Customer)


def create_Publisher(sender, instance, created, **kwargs):
    print("Saved Publisher is called")


signals.post_save.connect(receiver=create_Publisher, sender=Publisher)
