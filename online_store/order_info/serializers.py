from rest_framework import serializers
from order_info.models import Order
from product_cart.serializers import CartSerializer
from client_info.serializers import UserprofileSerializer
# Used to show ow much product is left at the warehouses
class OrderSerializer(serializers.HyperlinkedModelSerializer):
    cart_ordered = CartSerializer(read_only=True) #Correct????? Should this have a specific name 
    client = UserprofileSerializer(read_only=True)
    class Meta:
        model = Order
        fields = ['price', 'cart_ordered', 'client'] 


