from collections import OrderedDict

from django.conf.urls import url



ENDPOINTS = OrderedDict()

def add_endpoint(url, endpoint_class, fields=None):
    """
    Adds an endpoint

    >>> add_endpoint(r'products/', ProductList)
    """
    print "Register {}".format(url)
    fields = fields or {}
    ENDPOINTS[url] = dict(
        cls = endpoint_class,
        fields = fields,
    )

def remove_endpoint(url):
    """
    Removes all registered urls for an endpoint

    >>> remove_endpoint(r'products/')
    """
    del ENDPOINTS[url]

def remove_endpoints(endpoint_class):
    """
    Removes all registered urls for an endpoint

    >>> remove_endpoints(ProductList)
    """
    for url in list_endpoint_urls(endpoint_class):
        del ENDPOINTS[url]

def add_endpoint_field(endpoint_class, attr, field):
    """
    Adds a field to an endpoint
    """
    for url in list_endpoint_urls(endpoint_class):
        ENDPOINTS[url]['fields']

def remove_endpoint_field(endpoint_class, attr):
    """
    Removes a field from an endpoint
    """
    for url in list_endpoint_urls(endpoint_class):
        if attr in ENDPOINTS[url]['fields']:
            del ENDPOINTS[url]['fields'][attr]

def list_endpoint_urls(endpoint_class):
    """
    Lists the endpoint urls for the provided class
    """
    for url, item in ENDPOINTS.items():
        if item.get('cls') == endpoint_class:
            yield url

def all_endpoints():
    for url_path, cls in [(url_path, endpoint_config.get('cls')) for url_path, endpoint_config in ENDPOINTS.items()]:
        yield url(url_path, cls.as_view())

