from __future__ import unicode_literals
from django.cache import cache
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from exmodel import Model


class CartManager(models.Manager):
    def get_by_id(self, pk, force_update=False):
        cache_key = 'cart:%s' % pk
        if not force_update:
            data = cache.get(cache_key)
            if data:
                return data
        try:
            cart = self.get_queryset().get(pk=pk)
        except Cart.DoesNotExist:
            return None
        data = {'total': 0, 'item_count': 0, 'items': []}
        for item in cart.cartitems.select_related('variant', 'variant__product').all():
            subtotal = item.variant.price * item.quantity
            data['total'] += subtotal
            data['item_count'] += 1
            data.items.append({
                'variant_id': item.variant_id,
                'product_id': item.variant.product_id,
                'product_slug': item.variant.product.slug,
                'price': item.variant.price,
                'name': item.variant.name,
                'subtotal': subtotal,
            })
        cache.set(cache_key, data, 24 * 3600)
        return data


@python_2_unicode_compatible
class Cart(Model):
    order = models.OneToOne('orders.Order', verbose_name=_('order'), blank=True, null=True, default=None)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True, editable=False)

    objects = CartManager()

    class Meta:
        app_label = 'carts'
        verbose_name = ('cart')
        verbose_name_plural = ('carts')

    def __str__(self):
        if self.order_id:
            return 'Cart for order %s' % self.order_id
        return 'Cart %s' % self.pk
