from django.db import models

class Servicesss(models.Model):
    service_name = models.CharField(max_length = 150)
    price = models.CharField(max_length = 5)

    def __str__(self):
        return self.service_name

