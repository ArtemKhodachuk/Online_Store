from rest_framework import serializers
from warehouse_product_info.models import Productpresent
# Used to show ow much product is left at the warehouses 
class ProductpresentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Productpresent
        fields = ['name', 'quantity_left']
