from order_info.models import Order
from order_info.serializers import OrderSerializer
from rest_framework import generics
from rest_framework import permissions
from client_info.models import Userprofile
from order_info.permissions import IsOwner
from django.shortcuts import get_object_or_404


# look at the order 
class OrderView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Order, pk=pk)


class UserOrderView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Userprofile.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsOwner, permissions.IsAuthenticatedOrReadOnly] # Correct???
    
    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Userprofile, pk=pk).order
