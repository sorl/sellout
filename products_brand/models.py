from django.db import models
from sellout.base import extend_model


class Brand(models.Model):
    name = models.CharField(max_length=500)

    def __unicode__(self):
        return self.name


class ProductMixin(object):
    brand = models.ForeignKey(Brand)

    def __unicode__(self):
        return '%s -- %s' % (self.title, self.brand)


extend_model('products.Product', ProductMixin)
