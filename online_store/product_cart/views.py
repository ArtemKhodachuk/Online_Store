from django.shortcuts import render
from client_info.models import Userprofile
from rest_framework import generics
from product_cart.permissions import IsOwner
# Create your views here.
from product_cart.serializers import CartSerializer

#View for returning the user cart (Correct???????)
class UserCartView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Userprofile.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsOwner] # Correct???
    def get_object(self):
        pk = self.kwargs.get('pk')
        return Userprofile.objects.get(pk=pk).cart
