from django.db import models
from sellout.base import extend_model, ExtendableModel


class Brand(ExtendableModel):
    name = models.CharField(max_length=500)

    def __unicode__(self):
        return self.name


class ProductMixin(object):
    brand = models.ForeignKey(Brand)

    def __unicode__(self):
        return u'%s -- %s' % (self.title, self.brand)


class ProductShippingMixin(object):
    shippings = models.CharField(max_length=500)


extend_model(u'products.Product', ProductMixin)
extend_model(u'products.Product', ProductShippingMixin)
