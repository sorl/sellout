from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=500)

    def __unicode__(self):
        return self.title
