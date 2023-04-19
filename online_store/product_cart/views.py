from django.shortcuts import render
from client_info.models import Userprofile
from rest_framework import generics
from product_cart.permissions import IsOwner
from rest_framework import permissions
from product_cart.serializers import CartSerializer
from product_cart.models import Cart, CartItem
from django.shortcuts import get_object_or_404


#View for returning the user cart (Correct???????)
class UserCartView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Userprofile.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsOwner, permissions.IsAuthenticatedOrReadOnly] # Correct???

    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Userprofile, pk=pk).cart


class CartView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    
    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Cart, pk=pk)


# Correct use of the cartitemlist??
class InCartProductView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartItem

    def get_object(self):
        cart_id = self.kwargs.get('cart_id')
        pk = self.kwargs.get('pk')
        return get_object_or_404(CartItem, pk=pk, cart_id=cart_id) #How is this equvalent of the code below? How does a function know about the nested relationship?
        # cartitem_list = Cart.objects.get(pk=cart_id).cartitem_set
        # return cartitem_list.get(pk=pk)#Specifically is this correct
    