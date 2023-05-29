from rest_framework import serializers
from product_cart.models import CartItem, Cart


#Product in the cart
class CartItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name')
    product_price = serializers.IntegerField(source="product.price")

    class Meta:
        model = CartItem
        fields = ['product_name', 'product_price', 'quantity_incart']


#The actual cart serializer (just and array of productcarts above)
class CartSerializer(serializers.ModelSerializer):
    cartitem_set = CartItemSerializer(many=True)
    
    class Meta:
        model = Cart
        fields = ['cartitem_set']


