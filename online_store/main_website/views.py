from main_website.models import Userprofile, Productpresent, Productcart, Transaction
from main_website.serializers import UserprofileSerializer, ProductpresentSerializer, ProductcartSerializer, TransactiontSerializer
from rest_framework import generics
# Create your views here.
from rest_framework import permissions
from main_website.permissions import IsOwner
from rest_framework.response import Response

# Look at the user list
class UserView(generics.ListCreateAPIView):
    queryset = Userprofile.objects.all()
    serializer_class = UserprofileSerializer

# Look at the user cart
class UsercartView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Userprofile.objects.all()
    serializer_class = ProductcartSerializer
    def retrieve(self, request, *args, **kwargs): # Could not make get_object work in polls_to_rest (????????)
        pk = self.kwargs.get('pk')
        choices= Userprofile.objects.get(pk=pk).productcart_set
        serializer = ProductcartSerializer(choices, many=True)
        return Response(serializer.data)

# look at the product list
class ProductView(generics.ListCreateAPIView):
    queryset = Productpresent.objects.all()
    serializer_class = ProductpresentSerializer