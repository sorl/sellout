from django.db import models
from django.utils.translation import ugettext_lazy as _

from sellout.base import ExtendableModel


class Product(ExtendableModel):
    """
    Product Model
    """
    title = models.CharField(max_length=500)
    brand = models.CharField(max_length=500)
    shippings = models.ManyToManyField(Shipping)

    def __unicode__(self):
        return self.title

    class Meta:
        app_label = 'sellout'
        verbose_name = _('product')
        verbose_name_plural = _('products')

