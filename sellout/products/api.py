from sellout.api import add_endpoint
from sellout.api.modelviews import DetailEndpoint, ListEndpoint
from sellout.products.models import Product



class ProductList(ListEndpoint):
    """
    Product List Endpoint
    """
    model = Product

add_endpoint(r'^products/$', ProductList)



class ProductDetail(DetailEndpoint):
    """
    Product Detail Endpoint
    """
    model = Product

add_endpoint(r'^products/(?P<pk>\d+)$', ProductDetail)


