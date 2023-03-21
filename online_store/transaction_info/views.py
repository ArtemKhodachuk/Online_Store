from transaction_info.models import Transaction
from transaction_info.serializers import TransactiontSerializer
from rest_framework import generics
# Create your views here.


# Look at the transaction list
class TransactionView(generics.ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactiontSerializer