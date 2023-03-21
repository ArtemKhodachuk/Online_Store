from rest_framework import serializers
from cart_info.models import Productcart, Cart

#Product in the cart
class ProductcartSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Productcart
        fields = ['name', 'quantity_incart']

#The actual cart serializer (just and array of productcarts above)
class CartSerializer(serializers.HyperlinkedModelSerializer):
    productcart_set = ProductcartSerializer(many=True)
    class Meta:
        model = Cart
        fields = ['productcart_set']


