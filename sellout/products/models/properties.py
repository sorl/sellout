from django.db import models
from django.utils.translation import ugettext_lazy as _

from django_hstore.fields import DictionaryField

from sellout.base import ExtendableModel


class Properties(object):
    """
    Properties class
    """
    def __init__(self, *args, **kwargs):
        self._field = kwargs['field']
        self._field.set_default('items', [])
        self._all = None

    def __iter__(self):
        return self.all()

    def all(self):
        if self._all == None:
            property_ids = [x for x in self._field['items']]
            self._all = Property.objects.filter(id__in=property_ids)
        return self._all

    def add(self, prop):
        """
        Adds a property to the underlying field
        """
        if prop.id not in self._field['items']:
            self._field['items'].append(prop.id)
            self._all = None

    def remove(self, prop):
        """
        Removes a property from the underlying field
        """
        if prop.id in self._field['items']:
            self._field['items'].remove(prop.id)
            self._all = None



class Prototype(ExtendableModel):
    """
    Prototype Model
    """
    name = models.CharField(max_length=255)
    created_date = models.DateTimeField(_('created date'), auto_now_add=True, null=True, blank=True)
    modified_date = models.DateTimeField(_('modified date'), auto_now=True, null=True, blank=True)
    property_data = DictionaryField(_('properties'))

    def __init__(self, *args, **kwargs):
        super(Prototype, self).__init__(*args, **kwargs)
        self._properties = Properties(field=self.property_data)

    def __unicode__(self):
        return self.name

    @property
    def properties(self):
        """
        Gets all the properties
        """
        return self._properties

    @properties.setter
    def properties(self, values):
        """
        Sets all the properties
        """
        self.property_data['items'] = [x.id for x in values]
        self._properties = Properties(field=self.property_data)

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
        return self._value = value

    class Meta:
        app_label = 'sellout'
        verbose_name = _('property')
        verbose_name_plural = _('properties')



