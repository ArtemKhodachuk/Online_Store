from warehouse_product_info.models import Productpresent
from warehouse_product_info.serializers import ProductpresentSerializer
from rest_framework import generics
# Create your views here.

# look at the product list
class ProductView(generics.ListCreateAPIView):
    queryset = Productpresent.objects.all()
    serializer_class = ProductpresentSerializer