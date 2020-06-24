from django.db import models
from products.models import Product
from django.contrib.auth.models import User
import datetime


# 
class Order(models.Model):
    
    SUBMITTED = 'Submitted'
    PROCESSED =  'Processed'
    SHIPPED = 'Shipped'
    CANCELLED = 'Cancelled'
 
    STATUS_CHOICES = [
        (SUBMITTED, 'Submitted'),
        (PROCESSED, 'Processed'),
        (SHIPPED, 'Shipped'),
        (CANCELLED, 'Cancelled'),
    ]    

    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=50, blank=False)
    phone_number = models.CharField(max_length=20, blank=False)
    country = models.CharField(max_length=40, blank=False)
    postcode = models.CharField(max_length=20, blank=True)
    town_or_city = models.CharField(max_length=40, blank=False)
    street_address1 = models.CharField(max_length=40, blank=False)
    street_address2 = models.CharField(max_length=40, blank=False)
    county = models.CharField(max_length=40, blank=False)
    date_ordered = models.DateTimeField(default=datetime.datetime.today, null=True)
    total_quantity = models.IntegerField(blank=False)
    total_cost = models.IntegerField(blank=False)
    status = models.CharField(max_length=15,choices=STATUS_CHOICES,default=SUBMITTED)

    def __str__(self):
        return "{0}-{1}-{2}".format(self.id, self.customer, self.date_ordered)

    def get_absolute_url(self):
        return ('order_details', (), { 'order_id': self.id }) 

class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, null=False)
    product = models.ForeignKey(Product, null=False)
    quantity = models.IntegerField(blank=False)

    def __str__(self):
        return "{0} {1} @ {2}".format(
            self.quantity, self.product.title, self.product.price)