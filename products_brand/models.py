from django.db import models
from sellout.base import extend_model, ExtendableModel


class Brand(ExtendableModel):
    name = models.CharField(max_length=500)

    def __unicode__(self):
        return self.name


class ProductMixin(models.Model):
    brand = models.ForeignKey(Brand)

    def __unicode__(self):
        return u'%s -- %s' % (self.title, self.brand)

    class Meta:
        abstract = True


class ProductShippingMixin(models.Model):
    shippings = models.CharField(max_length=500)

    class Meta:
        abstract = True


extend_model(u'products.Product', ProductMixin)
extend_model(u'products.Product', ProductShippingMixin)
