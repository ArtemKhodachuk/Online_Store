from order_info.models import Order
from order_info.serializers import OrderSerializer
from rest_framework import generics
# Create your views here.

# look at the product list
class OrderView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer