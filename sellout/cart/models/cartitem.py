from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from exmodel import Model


@python_2_unicode_compatible
class CartItem(Model):
    cart = models.ForeignKey('carts.Cart', verbose_name=_('cart'), related_name='cartitems')
    variant = models.ForeignKey('products.Variant', verbose_name=_('variant'))
    quantity = models.PositiveIntegerField(_('quantity'), default=1)

    class Meta:
        app_label = 'carts'
        verbose_name = _('cart item')
        verbose_name_plural = _('cart items')

    @property
    def name(self):
        return self.variant.name

    @property
    def price(self):
        return self.variant.price

    @property
    def total(self):
        return self.price * self.quantity
