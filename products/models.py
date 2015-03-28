from django.db import models
from sellout.base import ExtendableModel


class Product(ExtendableModel):
    title = models.CharField(max_length=500)

    def __unicode__(self):
        return self.title
