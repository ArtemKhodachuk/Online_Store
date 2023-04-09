from django.db import models
from product_cart.models import Cart
# Create your models here.

# Used to show ow much product is left at the warehouses 
class Order(models.Model):
    price = models.IntegerField(default=0)
    cart_ordered = models.OneToOneField(Cart, related_name='cart', on_delete=models.CASCADE)



