from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from sellout.core.products.models import Product, OptionValue


@receiver(post_save, sender=Product)
def product_set_variant_name(sender, instance, **kwargs):
    for variant in instance.variants.select_related('product').all().prefetch_related('option_values'):
        variant.set_name()
        variant.save()  # that should trigger variant_clear_carts_cache


@receiver([post_save, post_delete], sender=OptionValue)
def optionvalue_set_variant_name(sender, instance, **kwargs):
    instance.variant.set_name()
    instance.variant.save()  # that should trigger variant_clear_carts_cache
