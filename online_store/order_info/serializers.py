from rest_framework import serializers
from order_info.models import Order
# Used to show ow much product is left at the warehouses
class OrderSerializer(serializers.HyperlinkedModelSerializer):
    cart_ordered = serializers.RelatedField(source='productincart_set', read_only=True)
    class Meta:
        model = Order
        fields = ['price', 'cart_ordered'] 


