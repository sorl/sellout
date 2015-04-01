
from django.apps import AppConfig

class SelloutConfig(AppConfig):
    name = 'sellout'
    verbose_name = 'Sellout'

    def ready(self):
        print "App loaded"
        #raise Exception("FUCK")

