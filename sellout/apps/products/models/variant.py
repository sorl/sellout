from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from exmodel import Model
from sellout.conf import settings


class VariantAvailableManager(models.Manager):
    def get_queryset(self):
        qs = super(VariantAvailableManager, self).get_queryset()
        return qs.filter(removed=False)


@python_2_unicode_compatible
class Variant(Model):
    removed = models.BooleanField(_('removed'), default=False)
    product = models.ForeignKey('products.Product', verbose_name=_('product'), related_name='variants')
    name = models.CharField(_('name'), max_length=500, ediable=False)  # set from product name and options
    sku = models.CharField(_('sku'), max_length=500, blank=True)
    price = models.FloatField(_('price'))
    tax_rate_percent = models.FloatField(_('tax rate'), blank=True, null=True, default=None, help_text=_('sales tax in percent, empty uses shop default rate'))
    stock_count = models.IntegerField(_('stock count'), default=10)
    position = models.IntegerField(_('position'), default=0)

    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True, editable=False)

    objects = models.Manager()
    available = VariantAvailableManager()

    class Meta:
        app_label = 'products'
        verbose_name = _('variant')
        verbose_name_plural = _('variants')
        ordering = ('position', 'created')

    def __str__(self):
        return self.name

    def get_tax_rate_percent(self):
        if self.tax_rate_precent is None:
            return settings.SELLOUT_DEFAULT_SALES_TAX_PERCENT
        return self.tax_rate_percent

    def set_name(self):
        """
        Sets the name for variant
        Should be triggered whenever product updates
        or any related option values
        """
        parts = [self.product.name]
        for v in self.option_values.all():
            parts.append(v.value)
        self.name = ' '.join(parts)
