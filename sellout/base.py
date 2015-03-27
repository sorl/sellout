#from django.apps import apps
#from django.conf import settings
from django.db.models.base import ModelBase


_mixin_registry = {}


def extend_model(model_name, mixin):
    print 'extend'
    #app_config = apps.get_containing_app_config(mixin.__module__)
    #app_label = app_config.label
    #if app_label in settings.INSTALLED_APPS:
    #    _mixin_registry.setdefault(model_name, {app_label: []})
    #    _mixin_registry[model_name][app_label].append(mixin)


class ExtendableMeta(ModelBase):
    def __new__(cls, name, bases, attrs):
        print 'allocate'
        #module = attrs['__module__']
        #app_config = apps.get_containing_app_config(module)
        #if app_config:
        #    model_name = '%s.%s' % (app_config.label, name)
        #    label_mixins = _mixin_registry.get(model_name)
        #    if label_mixins:
        #        bases = list(bases)
        #        for app_label in settings.INSTALLED_APPS:
        #            mixins = label_mixins.get(app_label)
        #            if mixins:
        #                bases.extend(mixins)
        #        bases = tuple(bases)
        return ModelBase.__new__(cls, name, bases, attrs)
