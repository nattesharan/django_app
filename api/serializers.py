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
class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    age = serializers.IntegerField(source='profile.age', required=False)
    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
            'username',
            'age'
        )

class PostSerializer(serializers.ModelSerializer):
    # so this is required only during fetching data or if we want to use that for creating also then we need to explicitly
    # write a create method
    posted_user_permissions = PermissionSerializer(many=True, required=False)
    class Meta:
        model = Post
        fields = (
            'id',
            'post',
            'user',
            'created_on',
            'posted_user_permissions',
        )
        # read_only_fields must be specified here default it takes foreign key
        # its not used while cresting data only used when reading data
        read_only_fields = ('user',)
        depth = 1
        # depth = 1 for one level
        # depth = 2 will give you second level and so on
    
    # we can do this if we want to create nested serializer data also
    # def create(self, validated_data):
    #     validated_data.pop('posted_user_permissions')
    #     post = Post.objects.create(**validated_data)
    #     return post

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

