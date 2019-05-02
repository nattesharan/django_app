from rest_framework import serializers
from django.contrib.auth.models import User
from home.models import Post
from django.contrib.auth import authenticate
from django.core.exceptions import ObjectDoesNotExist
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

class AddPermissionSerializer(serializers.Serializer):
    permissions = serializers.ListField(child = serializers.IntegerField())
    user = serializers.IntegerField()
    
    def validate(self, attrs):
        permissions = attrs.get('permissions',[])
        user = attrs.get('user','')
        if permissions and user:
            try:
                user = User.objects.get(pk=user)
                if not user.is_superuser:
                    permissions = Permission.objects.filter(pk__in=permissions)
                    attrs['permissions']= permissions
                    attrs['user']= user
                    return attrs
                raise serializers.ValidationError('User is already admin')
            except ObjectDoesNotExist:
                raise serializers.ValidationError('User not found')
        raise serializers.ValidationError('Permissons and user required')
