from django.cache import cache
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from sellout.apps.carts.models import Cart, CartItem
from sellout.apps.products.models import Variant


@receiver([post_save, post_delete], sender=CartItem)
def cartitem_update_cart_cache(sender, instance, **kwargs):
    Cart.objects.get_by_id(instance.cart_id, force_update=True)


@receiver([post_save, post_delete], sender=Variant)
def variant_clear_carts_cache(sender, instance, **kwargs):
    qs = Cart.objects.filter(cartitem__variant=instance)
    cart_ids = qs.distinct().values_list('pk', flat=True)
    for cart_id in cart_ids:
        cache.delete('cart:%s' % cart_id)
