from django.db import models
from sellout.base import ExtendableMeta


class Product(models.Model):
    __metaclass__ = ExtendableMeta

    title = models.CharField(max_length=500)

    def __unicode__(self):
        return self.title
