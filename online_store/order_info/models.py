from django.db import models
from product_cart.models import Cart
from client_info.models import Userprofile
# Create your models here.


# Used to show ow much product is left at the warehouses 
class Order(models.Model):
    price = models.IntegerField(default=0)
    cart_ordered = models.OneToOneField(Cart, related_name='order', on_delete=models.CASCADE)
    client = models.OneToOneField(Userprofile, related_name='order', on_delete=models.CASCADE, null=True)



