from django.db import models
from django.urls import reverse

class Product(models.Model):
    """ Model for product instances """

    MEN = "Men"
    WOMAN = "Woman"
    CHILDREN = "Children"
    SOUVENIRS = "Souvenirs"
    CATEGORY_CHOICES = [
        (MEN , "Men"),
        (WOMAN , "Woman"),
        (CHILDREN , "Children"),
        (SOUVENIRS , "Souvenirs"),
    ]
    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default=MEN,
    )
    title = models.CharField(max_length=100,blank=True)
    product_image1 = models.ImageField(upload_to="images", blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def get_absolute_url(self):
        """ Gets absolute url including id as pk for dynamic url """
        return reverse('product-detail', kwargs={'pk': self.id})

    def __str__(self):
        return self.title