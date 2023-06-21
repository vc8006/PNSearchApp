from django.db import models

class Dish(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    items = models.TextField()
    lat_long = models.CharField(max_length=100)
    full_details = models.TextField()

    def __str__(self):
        return self.name