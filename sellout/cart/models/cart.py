from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from exmodel import Model


data = {
    'items': [{
        'variant_id',
        'variant_url',
        'name',
        'quantity',
        'price',
        'subtotal',
    }],
    'total'
}


@python_2_unicode_compatible
class Cart(Model):
    order = models.OneToOne('orders.Order', verbose_name=_('order'), blank=True, null=True, default=None)
    data = JSONBField()
    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        app_label = 'carts'
        verbose_name = ('cart')
        verbose_name_plural = ('carts')

    def __str__(self):
        if self.order:
            return 'Cart for order %s' % self.order
        return 'Cart %s' % self.pk
