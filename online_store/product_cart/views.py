from django.shortcuts import render
from client_info.models import Userprofile
from rest_framework import generics
from product_cart.permissions import IsOwner
# Create your views here.
from product_cart.serializers import CartSerializer
from product_cart.models import Cart, CartItem

#View for returning the user cart (Correct???????)
class UserCartView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Userprofile.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsOwner] # Correct???
    def get_object(self):
        pk = self.kwargs.get('pk')
        return Userprofile.objects.get(pk=pk).cart

class CartView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

# Correct use of the cartitemlist??
class InCartProductView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartItem
    def get_object(self):
        cart_id = self.kwargs.get('cart_id')
        pk = self.kwargs.get('pk')
        cartitem_list = Cart.objects.get(pk=cart_id).cartitem_set
        return cartitem_list.get(pk=pk)#Specifically is this correct
    