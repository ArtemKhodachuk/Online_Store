from rest_framework import serializers
from django.contrib.auth.models import User
from transaction_info.models import Transaction 

# Transaction information that is stored and viewed latter 
class TransactiontSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Transaction
        fields = ['username', 'product_name', 'quantity_bought']

