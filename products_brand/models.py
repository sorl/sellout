from django.db import models
from products.models import Product


class Product(Product):
    brand = models.CharField(max_length=500)

    def __unicode__(self):
        return '%s -- %s' % (self.title, self.brand)
