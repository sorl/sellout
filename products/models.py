from django.db import models
from sellout.base import ExtendableModel


class Shipping(ExtendableModel):
    name = models.CharField(max_length=500)


class Product(ExtendableModel):
    title = models.CharField(max_length=500)
    brand = models.CharField(max_length=500)
    shippings = models.ManyToManyField(Shipping)

    def __unicode__(self):
        return self.title
