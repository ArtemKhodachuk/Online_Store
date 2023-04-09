from django.shortcuts import render
from client_info.models import Userprofile
from rest_framework import generics
from product_cart.permissions import IsOwner
# Create your views here.
from product_cart.serializers import CartSerializer
from product_cart.models import Cart, ProductInCart

#View for returning the user cart (Correct???????)
class UserCartView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Userprofile.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsOwner] # Correct???
    def get_object(self):
        pk = self.kwargs.get('pk')
        return Userprofile.objects.get(pk=pk).cart

class CartView(generics.ListCreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = ProductInCart
    def get_queryset(self):
        cart_id = self.kwargs.get('cart_id')
        return Cart.objects.get(pk=cart_id).productincart_set

# Correct if ingnoring cart_id?
class InCartProductView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductInCart.objects.all()
    serializer_class = ProductInCart
    