import six

from restless import views

from sellout.api.auth import login_required, admin_required


class EndpointMetaClass(type):
    """
    Meta class for Endpoint models
    """
    def __new__(cls, name, bases, attrs):
        super_new = super(EndpointMetaClass, cls).__new__
        obj = super_new(cls, name, bases, attrs)

        verbs = attrs.get('admin_required', [])
        for verb in verbs:
            if hasattr(obj, verb):
                decorated_func = admin_required(getattr(obj, verb))
                setattr(obj, verb, decorated_func)
        verbs = attrs.get('login_required', [])
        for verb in verbs:
            setattr(obj, verb) = login_required(getattr(obj, verb))
        return obj

class EndpointMixin(object):
    """
    Mixes in some field functionality that we want
    """
    def _get(self, request, *args, **kwargs):
        return super(EndpointMixin, self).get(request, *args, **kwargs)

class Endpoint(six.with_metaclass(EndpointMetaClass, views.Endpoint)):
    pass

