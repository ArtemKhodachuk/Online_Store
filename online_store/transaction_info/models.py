from django.db import models

# Create your models here.

# Transaction information that is stored and viewed latter 
class Transaction(models.Model):
    username =  models.CharField(max_length=200)
    product_name = models.CharField(max_length=200)
    quantity_bought = models.IntegerField(default=1)



