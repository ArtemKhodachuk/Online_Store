from order_info.models import Order
from order_info.serializers import OrderSerializer
from rest_framework import generics
# Create your views here.
from client_info.models import Userprofile
from product_cart.permissions import IsOwner
# look at the order 
class OrderView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class UserOrderView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Userprofile.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsOwner] # Correct???
    def get_object(self):
        pk = self.kwargs.get('pk')
        return Userprofile.objects.get(pk=pk).order
