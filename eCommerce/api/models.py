from django.db import models


class Product(models.Model):
    TITLE_MAX_LENGTH = 20
    PRICE_MAX_DIGITS = 12
    PRICE_MAX_DECIMAL_PLACES = 2
    title = models.CharField(
        max_length=TITLE_MAX_LENGTH)
    price = models.DecimalField(
        max_digits=PRICE_MAX_DIGITS,
        decimal_places=PRICE_MAX_DECIMAL_PLACES)

    def __str__(self):
        return f'{self.title}{self.pk}'


class Order(models.Model):
    date = models.DateField()
    products = models.ManyToManyField(Product)

    def __str__(self):
        return f'{self.pk}'
