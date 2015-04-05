from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from exmodel import Model


class VariantManager(models.Manager):
    def get_queryset(self):
        qs = super(VariantManager, self).get_queryset()
        return qs.select_related('product').prefetch_related('option_values__option')


class VariantAvailableManager(VariantManager):
    def get_queryset(self):
        qs = super(VariantAvailableManager, self).get_queryset()
        return qs.filter(removed=False)


@python_2_unicode_compatible
class Variant(Model):
    removed = models.BooleanField(_('removed'), default=False)
    product = models.ForeignKey('Product', verbose_name=_('product'), related_name='variants')
    sku = models.CharField(_('sku'), max_length=500, blank=True)
    price = models.FloatField(_('price'))
    stock_count = models.IntegerField(_('stock count'), default=10)
    position = models.IntegerField(_('position'), default=0)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True, editable=False)

    objects = VariantManager()
    _objects = models.Manager()
    available = VariantAvailableManager()

    class Meta:
        app_label = 'products'
        verbose_name = _('variant')
        verbose_name_plural = _('variants')
        ordering = ('position', 'created')

    def __str__(self):
        return '%s %s' % (self.product, self.sku)


@python_2_unicode_compatible
class Option(models.Model):
    name = models.CharField(_('name'), max_length=500)
    position = models.IntegerField(_('position'), default=0)

    class Meta:
        app_label = 'products'
        verbose_name = _('option')
        verbose_name_plural = _('options')
        ordering = ('position', 'name')

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class OptionValue(models.Model):
    variant = models.ForeignKey('Variant', verbose_name=_('variant'), related_name='option_values')
    option = models.ForeignKey('Option', verbose_name=_('option'))
    value = models.CharField(_('value'), max_length=500)
    position = models.IntegerField(_('position'), default=0)

    class Meta:
        app_label = 'products'
        verbose_name = _('option value')
        verbose_name_plural = _('option value')
        unique_together = (('variant', 'option'),)
        ordering = ('position',)

    def __str__(self):
        return '%s - %s' % (self.option, self.value)
