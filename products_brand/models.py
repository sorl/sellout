from django.db import models
from sellout.base import extend_model


class Brand(models.Model):
    name = models.CharField(max_length=500)

    def __unicode__(self):
        return self.name


class ProductMixin(models.Model):
    #brand = models.ForeignKey(Brand)
    brand = models.CharField(max_length=500)

    def __unicode__(self):
        return '%s -- %s' % (self.title, self.brand)

    class Meta:
        abstract = True


extend_model('products.Product', ProductMixin)
