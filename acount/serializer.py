from rest_framework import serializers
from django.contrib.auth.models import User
#from .serializer import TodoUsersSerializer


class TodoUsersSerializer(serializers.ModelSerializer):
    
    username = serializers.CharField()

    class Meta:
        model = User
        fields = [
            
            'username',
            'email'
        ]
       