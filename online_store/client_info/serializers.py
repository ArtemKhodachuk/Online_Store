from rest_framework import serializers
from django.contrib.auth.models import User
from client_info.models import Userprofile

#Default user implemenattion
class UserSerializer(serializers.HyperlinkedModelSerializer):
    user_profile = serializers.HyperlinkedRelatedField(view_name='UserProfile', read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'user_profile']

#User profile, using the default user implementation 
class UserprofileSerializer(serializers.HyperlinkedModelSerializer):
    user_id = serializers.ReadOnlyField(source='owner.id')
    username = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Userprofile
        fields = ['user_id', 'username']


