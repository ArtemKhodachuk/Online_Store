from django.db import models
from client_info.models import Userprofile
# Create your models here.

# The Actual Cart
class Cart(models.Model):
    client_owner = models.OneToOneField(Userprofile, related_name='cart', on_delete=models.CASCADE)

# Product designated as being in cart 
class Productcart(models.Model):
    name = models.CharField(max_length=200)
    quantity_incart = models.IntegerField(default=1)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
