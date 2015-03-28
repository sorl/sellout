import six
from django.apps import apps
from django.conf import settings
from django.db.models.base import ModelBase
from django.db import models
from django.db.models.fields import Field
from itertools import chain


_mixin_registry = {}


def extend_model(model_name, mixin):
    """
    Registers a mixin a model_name passed as module.Model
    """
    app_config = apps.get_containing_app_config(mixin.__module__)
    app_label = app_config.label
    # we only add the mixin class if its app_label is in installed apps
    if app_label in settings.INSTALLED_APPS:
        _mixin_registry.setdefault(model_name, {})
        _mixin_registry[model_name].setdefault(app_label, [])
        _mixin_registry[model_name][app_label].append(mixin)


def get_registered_mixins(module, name):
    """
    Get all the registered mixins for the model name in the passed module
    """
    all_mixins = []
    app_config = apps.get_containing_app_config(module)
    if app_config:
        model_name = '%s.%s' % (app_config.label, name)
        label_mixins = _mixin_registry.get(model_name)
        if label_mixins:
            # we get the mixins in the order of installed apps
            for app_label in settings.INSTALLED_APPS:
                mixins = label_mixins.get(app_label)
                if mixins:
                    all_mixins.extend(mixins)
    return all_mixins


def merge_attrs(mixins, attrs):
    """
    pops and returns model fields in attrs
    """
    #
    # TODO megre methods and meta attributes
    #
    fields = {}
    for mixin in mixins:
        mixin_fields = chain(
            mixin._meta.local_fields,
            mixin._meta.local_many_to_many,
            mixin._meta.virtual_fields,
        )
        for f in mixin_fields:
            if f.name not in fields:
                fields[f.name] = f
    for k, v in attrs.items():
        if isinstance(v, Field):
            attrs.pop(k)
            if k not in fields:
                fields[k] = v
    attrs.update(fields)


class ExtendableMeta(ModelBase):
    def __new__(cls, name, bases, attrs):
        module = attrs['__module__']
        mixins = get_registered_mixins(module, name)
        merge_attrs(mixins, attrs)
        model = ModelBase.__new__(cls, name, bases, attrs)
        return model


class ExtendableModel(six.with_metaclass(ExtendableMeta, models.Model)):
    class Meta:
        abstract = True
