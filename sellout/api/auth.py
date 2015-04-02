
from restless.auth import login_required


def admin_required(fn):
    """
    Decorator for :py:class:`restless.views.Endpoint` methods to require
    authenticated, active user. If the user isn't authenticated, HTTP 403 is
    returned immediately (HTTP 401 if Basic HTTP authentication is used).
    """
    def wrapper(self, request, *args, **kwargs):
        if request.user is None or not request.user.is_active or not request.user.is_superuser:
            if isinstance(self, BasicHttpAuthMixin):
                return Http401()
            else:
                return Http403('forbidden')
        return fn(self, request, *args, **kwargs)
    wrapper.__name__ = fn.__name__
    wrapper.__doc__ = fn.__doc__
    return wrapper
