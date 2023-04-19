from product.models import ProductPresent
from product.serializers import ProductpresentSerializer
from rest_framework import generics
from rest_framework import filters
from django.shortcuts import get_object_or_404
# Create your views here.


# look at the product list
class ProductListView(generics.ListCreateAPIView):
    queryset = ProductPresent.objects.all()
    serializer_class = ProductpresentSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

class ProductView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductPresent.objects.all()
    serializer_class = ProductpresentSerializer

    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(ProductPresent, pk=pk)