from django.db import models
from django.utils.translation import ugettext_lazy as _
from exmodel import Model


class Product(Model):
    """
    Product Model
    """
    title = models.CharField(max_length=500)
    brand = models.CharField(max_length=500)

    def __unicode__(self):
        return self.title

    class Meta:
        app_label = 'sellout'
        verbose_name = _('product')
        verbose_name_plural = _('products')
