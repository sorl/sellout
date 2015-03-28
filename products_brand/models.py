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


class BogusMeta1(type):
    def __new__(cls, name, bases, attrs):
        print 'allocating bogus nr 1'
        return type.__new__(cls, name, bases, attrs)


class BogusMeta2(type):
    def __new__(cls, name, bases, attrs):
        print 'allocating bogus nr 2'
        return type.__new__(cls, name, bases, attrs)


class Bogus1(object):
    __metaclass__ = BogusMeta1
extend_model('products.Product', ProductMixin)
class Bogus2(object):
    __metaclass__ = BogusMeta2
