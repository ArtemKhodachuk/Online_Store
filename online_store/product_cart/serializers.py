from rest_framework import serializers
from product_cart.models import ProductInCart, Cart

#Product in the cart
class ProductInCartSerializer(serializers.HyperlinkedModelSerializer):
    product_name = serializers.CharField(source='product.name')
    product_price = serializers.IntegerField(source="product.price")
    class Meta:
        model = ProductInCart
        fields = ['product_name', 'quantity_incart']

#The actual cart serializer (just and array of productcarts above)
class CartSerializer(serializers.HyperlinkedModelSerializer):
    productincart_set = ProductInCartSerializer(many=True)
    class Meta:
        model = Cart
        fields = ['productincart_set']


