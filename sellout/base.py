import six
from django.apps import apps
from django.conf import settings
from django.db.models.base import ModelBase
from django.db import models


_mixin_registry = {}


def extend_model(model_name, mixin):
    app_config = apps.get_containing_app_config(mixin.__module__)
    app_label = app_config.label
    # we only add the mixin class if its app_label is in installed apps
    if app_label in settings.INSTALLED_APPS:
        _mixin_registry.setdefault(model_name, {app_label: []})
        _mixin_registry[model_name][app_label].append(mixin)


class ExtendableMeta(ModelBase):
    def __new__(cls, name, bases, attrs):
        module = attrs['__module__']
        app_config = apps.get_containing_app_config(module)
        if app_config:
            model_name = '%s.%s' % (app_config.label, name)
            label_mixins = _mixin_registry.get(model_name)
            if label_mixins:
                bases = list(bases)
                # we load the mixins in the order of installed apps
                for app_label in settings.INSTALLED_APPS:
                    mixins = label_mixins.get(app_label)
                    if mixins:
                        bases.extend(mixins)
                bases = tuple(bases)
        return ModelBase.__new__(cls, name, bases, attrs)


class ExtendableModel(six.with_metaclass(ExtendableMeta, models.Model)):
    class Meta:
        abstract = True
