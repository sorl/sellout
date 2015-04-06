from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from sellout.products.models import Variant


@receiver([post_save, post_delete], sender=Variant)
def variant_count(cls, obj, **kwargs):
    obj.product.variant_count = Variant.objects.filter(product=obj.product).count()
    obj.product.save()
