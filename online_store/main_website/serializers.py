from rest_framework import serializers
from django.contrib.auth.models import User
from main_website.models import Userprofile, Productpresent, Productcart, Transaction 
# Used to show ow much product is left at the warehouses 
class ProductpresentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Productpresent
        fields = ['name', 'quantity_left']
#Producst that are placed in the cart of a particular user
class ProductcartSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Productcart
        fields = ['name', 'quantity_incart']
#Default user implemenattion
class UserSerializer(serializers.HyperlinkedModelSerializer):
    user_profile = serializers.HyperlinkedRelatedField(view_name='UserProfile', read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'user_profile']
#User profile, using the default user implementation (?????????)
class UserprofileSerializer(serializers.HyperlinkedModelSerializer):
    user_id = serializers.ReadOnlyField(source='owner.id')
    username = serializers.ReadOnlyField(source='owner.username')
    cart_set = ProductcartSerializer(many=True, read_only=True)
    class Meta:
        model = Userprofile
        fields = ['user_id', 'username', 'cart_set']

# Transaction information that is stored and viewed latter 
class TransactiontSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Transaction
        fields = ['username', 'product_name', 'quantity_bought']

