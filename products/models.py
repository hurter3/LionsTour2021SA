from django.db import models
from django.urls import reverse

class Product(models.Model):
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images')

    def get_absolute_url(self):
        """ Gets absolute url including id as pk for dynamic url """
        return reverse('product-detail', kwargs={'pk': self.id})


    def __str__(self):
        return self.name