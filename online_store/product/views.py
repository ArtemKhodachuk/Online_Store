from product.models import ProductPresent
from product.serializers import ProductpresentSerializer
from rest_framework import generics
# Create your views here.

# look at the product list
class ProductView(generics.ListCreateAPIView):
    queryset = ProductPresent.objects.all()
    serializer_class = ProductpresentSerializer