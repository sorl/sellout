from django.db import models
from django.utils.translation import ugettext_lazy as _

from exmodel import Model



class Prototype(Model):
    """
    Prototype Model
    """
    name = models.CharField(max_length=255)
    created_date = models.DateTimeField(_('created date'), auto_now_add=True, null=True, blank=True)
    modified_date = models.DateTimeField(_('modified date'), auto_now=True, null=True, blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
        app_label = 'sellout'
        verbose_name = _('prototype')
        verbose_name_plural = _('prototypes')


class Property(Model):
    """
    Property Model
    """
    name = models.CharField(max_length=255)
    created_date = models.DateTimeField(_('created date'), auto_now_add=True, null=True, blank=True)
    modified_date = models.DateTimeField(_('modified date'), auto_now=True, null=True, blank=True)

    def __init__(self, *args, **kwargs):
        self._value = None
        super(Property, self).__init__(*args, **kwargs)

    def __unicode__(self):
        return self.name

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    class Meta:
        app_label = 'sellout'
        verbose_name = _('property')
        verbose_name_plural = _('properties')


class PrototypeProperty(Model):
    """
    Prototype Property Model
    """
    property = models.ForeignKey('Property', verbose_name=_('property'), related_name='prototypes', db_index=True)
    prototype = models.ForeignKey('Prototype', verbose_name=_('prototype'), related_name='properties', db_index=True)
    position = models.IntegerField()

    def __unicode__(self):
        return u"{}.{}".format(self.prototype.name, self.property.name)

    class Meta:
        app_label = 'sellout'
        verbose_name = _('prototype property')
        verbose_name_plural = _('prototype properties')
        unique_together = ('prototype', 'property')


class ProductProperty(Model):
    """
    Product Property Model
    """
    property = models.ForeignKey('Property', verbose_name=_('property'), related_name='products', db_index=True)
    product = models.ForeignKey('Product', verbose_name=_('product'), related_name='properties', db_index=True)
    value = models.CharField(_('value'), max_length=255)
    position = models.IntegerField()

    def __unicode__(self):
        return u"{}.{}".format(self.product.name, self.property.name)

    class Meta:
        app_label = 'sellout'
        verbose_name = _('product property')
        verbose_name_plural = _('product properties')
        unique_together = ('product', 'property')


