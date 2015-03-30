from django.db import models
from django.utils.translation import ugettext_lazy as _

from sellout.base import ExtendableModel


class Prototype(ExtendableModel):
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



class Property(ExtendableModel):
    """
    Property Model
    """
    name = models.CharField(max_length=255)
    created_date = models.DateTimeField(_('created date'), auto_now_add=True, null=True, blank=True)
    modified_date = models.DateTimeField(_('modified date'), auto_now=True, null=True, blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
        app_label = 'sellout'
        verbose_name = _('property')
        verbose_name_plural = _('properties')


