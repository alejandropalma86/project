from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Todo

class TodoListSerializer(serializers.ModelSerializer):
    title = serializers.CharField()
    done = serializers.BooleanField()
    # created_date = serializers.DateTimeField()
    # modified_date = serializers.DateTimeField()
    #username = serializers.CharField(source='user.username')

    class Meta:
        model = Todo
        fields = [
            'id',
            'title',
            'user',
            #'done',
            #'created_date',
            #'modified_date',
            #'username',
            
        ]
       
class TodoRetrieveSerializer(TodoListSerializer):
    class Meta:
        model = Todo
        fields = TodoListSerializer.Meta.fields + [
            
            'done',
            'created_date',
            'modified_date',
            #'username',
            
        ]


       