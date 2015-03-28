import six
from django.apps import apps
from django.conf import settings
from django.db.models.base import ModelBase
from django.db import models
from django.db.models.fields import Field


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


def merge_mixins(mixins, attrs):
    """
    Merges attrs from all mixins in to attrs
    """
    #
    # TODO make sure meta attributes are correctly transferred
    # or maybe not? What do we want besides fields and normal methods?
    #
    new_attrs = {}
    not_keys = dict(object.__dict__).keys() + ['__dict__', '__module__', '__weakref__']
    if mixins:
        Mixins = type('Mixins', tuple(mixins), {})
        for k in dir(Mixins):
            if k not in not_keys:
                new_attrs[k] = getattr(Mixins, k)
    attrs.update(new_attrs)


class ExtendableMeta(ModelBase):
    def __new__(cls, name, bases, attrs):
        module = attrs['__module__']
        mixins = get_registered_mixins(module, name)
        merge_mixins(mixins, attrs)
        model = ModelBase.__new__(cls, name, bases, attrs)
        return model


class ExtendableModel(six.with_metaclass(ExtendableMeta, models.Model)):
    class Meta:
        abstract = True
