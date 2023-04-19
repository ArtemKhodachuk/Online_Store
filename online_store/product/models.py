from django.db import models

# Create your models here.


# Used to show ow much product is left at the warehouses 
class ProductPresent(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField(default=0)
    quantity_left = models.IntegerField(default=0)


class ProductImage(models.Model):
    pic_name = models.CharField(max_length=200)
    image = models.ImageField(upload_to ='uploads/% Y/% m/% d/') # Should I put somthing here??
    product = models.ForeignKey(ProductPresent, on_delete=models.CASCADE)


