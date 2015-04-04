import six

from restless import views

from sellout.api import auth


class EndpointMetaClass(type):
    """
    Meta class for Endpoint models
    """
    def __new__(cls, name, bases, attrs):
        super_new = super(EndpointMetaClass, cls).__new__
        obj = super_new(cls, name, bases, attrs)

        # Support for the following syntax on endpoints:
        #
        #   `admin_required = ['put', 'delete']`
        #   `login_required = ['get',]`
        func_names = ['login_required', 'admin_required']
        for func_name in func_names:
            verbs = attrs.get(func_name,[])
            for verb in verbs:
                if hasattr(obj, verb):
                    decorator_func = getattr(auth, func_name)
                    decorated_func =  decorator_func(getattr(obj, verb))
                    setattr(obj, verb, decorated_func)
        return obj

class EndpointMixin(object):
    """
    Mixes in some field functionality that we want
    """
    def get(self, request, *args, **kwargs):
        return super(EndpointMixin, self).get(request, *args, **kwargs)

class Endpoint(six.with_metaclass(EndpointMetaClass, views.Endpoint)):
    pass

