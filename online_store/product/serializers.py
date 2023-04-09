from rest_framework import serializers
from product.models import ProductPresent, ProductImage
# Used to show ow much product is left at the warehouses
class ProductImageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['pic_name', 'image'] 

class ProductpresentSerializer(serializers.HyperlinkedModelSerializer):
    productimage_set = ProductImageSerializer(many=True)
    class Meta:
        model = ProductPresent
        fields = ['name', 'quantity_left', 'productimage_set']
