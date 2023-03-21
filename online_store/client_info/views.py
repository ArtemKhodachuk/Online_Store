from django.shortcuts import render
from client_info.models import Userprofile
from client_info.serializers import UserprofileSerializer
from rest_framework import generics
# Create your views here.

# Create your views here.
class UserView(generics.ListCreateAPIView):
    queryset = Userprofile.objects.all()
    serializer_class = UserprofileSerializer