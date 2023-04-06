from rest_framework import serializers
from product.models import ProductPresent
# Used to show ow much product is left at the warehouses 
class ProductpresentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProductPresent
        fields = ['name', 'quantity_left']
