from django.db import models


# Create your models here.
class Shop(models.Model):
    shop_name = models.CharField(max_length=255)
    contact = models.BigIntegerField()
    location = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    contact_person = models.CharField(max_length=255)
    email = models.EmailField()
    image = models.ImageField(default='test.jpeg', null=True, upload_to='event/')



class Product(models.Model):
    product_name = models.CharField(max_length=255)
    price = models.IntegerField()
    discount = models.FloatField()
    old_price = models.IntegerField()


class Deal(models.Model):
    deal_name = models.CharField(max_length=255)
    valid_from = models.DateField()
    valid_till = models.DateField()
    discount_percent = models.FloatField()

class Event(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateField()
    venue = models.CharField(max_length=255)
    manager = models.CharField(max_length=255)
    description = models.TextField()

# hamle forgen key halnu paryo haina
