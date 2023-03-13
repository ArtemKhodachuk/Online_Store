from django.db import models

# Create your models here.

# Used to show ow much product is left at the warehouses 
class Productpresent(models.Model):
    name = models.CharField(max_length=200)
    quantity_left = models.IntegerField(default=0)

#User profile to which the user must login
class Userprofile(models.Model):
    owner = models.ForeignKey('auth.User', related_name='UserProfile', on_delete=models.CASCADE)

#Producst that are placed in the cart of a particular user
class Productcart(models.Model):
    name = models.CharField(max_length=200)
    quantity_incart = models.IntegerField(default=1)
    user = models.ForeignKey(Userprofile, on_delete=models.CASCADE)

# Transaction information that is stored and viewed latter 
class Transaction(models.Model):
    username =  models.CharField(max_length=200)
    product_name = models.CharField(max_length=200)
    quantity_bought = models.IntegerField(default=1)



