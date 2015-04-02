from sellout.api import add_endpoint
from sellout.api.auth import admin_required
from sellout.api.modelviews import DetailEndpoint, ListEndpoint
from sellout.core.products.models import Product, Prototype



class ProductList(ListEndpoint):
    """
    Product List Endpoint
    """
    model = Product
    admin_required = ['post']

add_endpoint(r'^products/$', ProductList)



class ProductDetail(DetailEndpoint):
    """
    Product Detail Endpoint
    """
    model = Product
    admin_required = ['delete', 'put']

add_endpoint(r'^products/(?P<pk>\d+)$', ProductDetail)



class PrototypeList(ListEndpoint):
    """
    Prototype List Endpoint
    """
    model = Prototype
    admin_required = ['post']

add_endpoint(r'^prototypes/$', PrototypeList)



class PrototypeDetail(DetailEndpoint):
    """
    Prototype Detail Endpoint
    """
    model = Prototype
    admin_required = ['delete', 'put']

add_endpoint(r'^prototypes/(?P<pk>\d+)$', PrototypeDetail)



