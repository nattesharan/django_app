from rest_framework import serializers
from django.contrib.auth.models import User
from home.models import Post
from django.contrib.auth import authenticate
from django.contrib.auth.models import Permission


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
    user = serializers.ReadOnlyField(source='user.pk')
    class Meta:
        model = Post
        fields = (
            'id',
            'post',
            'user',
            'created_on'
        )

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        username = data.get('username',None)
        password = data.get('password', None)

        if username and password:
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    data['user'] = user
                    return data
                else:
                    msg = 'User not active.'
                    raise serializers.ValidationError(msg)
            else:
                msg = 'Invalid credentials.'
                raise serializers.ValidationError(msg)
        else:
            msg = "Username and password not found."
            raise serializers.ValidationError(msg)

class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = '__all__'