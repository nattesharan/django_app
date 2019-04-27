from rest_framework import serializers
from django.contrib.auth.models import User
from home.models import Post


'''
serializers.Serializer:
Normal serializer means we need to create our own fields and validations 
UseCase: If we want to send a different response to the user or get differnt body from the request in this case
its better we use THis
serializers.ModelSerializer:
When we have a model and we need to perform basic crud on the model in this case we use ModelSerializer

'''
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
            'username'
        )

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'post',
            'user',
            'created_on'
        )