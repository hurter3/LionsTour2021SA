from django.db import models
from django.urls import reverse

class Product(models.Model):
    """ Model for product instances """

    MENS = "Men's"
    WOMANS = "Woman's"
    CHILDREN = "Children"
    SOUVENIRS = "Souvenir's"
    CATEGORY_CHOICES = [
        (MENS , "Men's"),
        (WOMANS , "Woman's"),
        (CHILDREN , "Children"),
        (SOUVENIRS , "Souvenir's"),
    ]
    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default=MENS,
    )
    title = models.CharField(max_length=100,blank=True)
    product_image1 = models.ImageField(upload_to="images", blank=True)
    product_image2 = models.ImageField(upload_to="images", blank=True, null=True)
    product_image3 = models.ImageField(upload_to="images", blank=True, null=True)
    product_image4 = models.ImageField(upload_to="images", blank=True, null=True)
    product_image5 = models.ImageField(upload_to="images", blank=True, null=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    stock_qty = models.IntegerField(default=0)
    available = models.BooleanField(default=False)

    def get_absolute_url(self):
        """ Gets absolute url including id as pk for dynamic url """
        return reverse('product-detail', kwargs={'pk': self.id})

    def __str__(self):
        return self.title