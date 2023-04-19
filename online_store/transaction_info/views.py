from transaction_info.models import Transaction
from transaction_info.serializers import TransactiontSerializer
from rest_framework import generics
from django.shortcuts import get_object_or_404
# Create your views here.


# Look at the transaction list
class TransactionListView(generics.ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactiontSerializer


class TransactionView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactiontSerializer

    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Transaction, pk=pk)