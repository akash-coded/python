# drfapp/api/models.py
from django.db import models


class Country(models.Model):
    country_name = models.CharField(max_length=20)
    local_currency = models.CharField(max_length=20)
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.country_name
