import six
from restless import modelviews

from sellout.api.views import EndpointMetaClass



class ListEndpoint(six.with_metaclass(EndpointMetaClass, modelviews.ListEndpoint)):
    pass



class DetailEndpoint(six.with_metaclass(EndpointMetaClass, modelviews.DetailEndpoint)):
    pass

