from rest_framework import viewsets
from django.contrib.auth.models import User
from api.serializers import UserSerializer, PostSerializer, LoginSerializer
from home.models import Post
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, mixins
# import the login schemes
from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework.decorators import authentication_classes, permission_classes
# auth classess have no affect without permission classess
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.contrib.auth import login, logout
from rest_framework.authtoken.models import Token

#import jwt authentication
from rest_framework_simplejwt.authentication import JWTAuthentication



# we use view sets when we want a view or we want all the crud to be implemented without any other operations
class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = (TokenAuthentication, BasicAuthentication, JWTAuthentication)
    permission_classes = (IsAuthenticated, IsAdminUser)


# we can also use generics and mixins for creting apis its combination of ViewSet and APIView
# Save and deletion hooks:

# The following methods are provided by the mixin classes, and provide easy overriding of the object save or deletion behavior.

# perform_create(self, serializer) - Called by CreateModelMixin when saving a new object instance.
# perform_update(self, serializer) - Called by UpdateModelMixin when saving an existing object instance.
# perform_destroy(self, instance) - Called by DestroyModelMixin when deleting an object instance.
class PostsGenericView(generics.GenericAPIView, 
                        mixins.ListModelMixin, 
                        mixins.CreateModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.DestroyModelMixin):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    authentication_classes = (TokenAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)
    # if we dont want pk as url parameter we can add a lookup field
    # lookup_field = 'id'
    # if we want to use some other field for querying like slugs

    def get(self, request, pk=None):
        if pk:
            return self.retrieve(request)
        return self.list(request)
    
    def post(self, request, pk=None):
        return self.create(request)
    
    def perform_create(self, serializer):
        serializer.save(user=User.objects.get(pk=2))
    
    def put(self, request, pk):
        return self.update(request)
    
    def perform_update(self, serializer):
        serializer.save(user=User.objects.get(pk=2))

    def delete(self, request, pk):
        return self.destroy(request)


class PostsApiView(APIView):
    # the main advantage of using class over functional view is no need to worry about parsing !!!! Hurrayyyyy !!! 
    def get(self, request, pk=None):
        posts = Post.objects.all()
        if pk:
            try:
                post = posts.get(pk=pk)
            except ObjectDoesNotExist:
                return Response({'error': 'Post not found with {}'.format(pk)}, status=404)
            post = PostSerializer(post)
            return Response(post.data)
        posts = Post.objects.all()
        posts = PostSerializer(posts, many=True)
        return Response(posts.data)

    def post(self, request, pk=None):
        if pk:
            return Response({'error': 'Unhandled Method !!'}, status=403)
        # there is no need for us to do parsing as APIView does it for us !! Thanks APIView.....
        data = request.data
        post = PostSerializer(data=data)
        if post.is_valid():
            post.save()
            return Response(post.data, status=201)
        return Response(post.errors, status=400)
    
    def put(self, request, pk=None):
        if not pk:
            return Response({'error': 'Unhandled Method !!'}, status=403)
        try:
            post = Post.objects.get(pk=pk)
        except ObjectDoesNotExist:
            return JsonResponse({'error': 'Post not found with {}'.format(pk)}, status=404)
        data = request.data
        post = PostSerializer(post, data=data)
        if post.is_valid():
            post.save()
            return Response(post.data)
    
    def delete(self, request, pk=None):
        if not pk:
            return Response({'error': 'Unhandled Method !!'}, status=403)
        try:
            post = Post.objects.get(pk=pk)
        except ObjectDoesNotExist:
            return JsonResponse({'error': 'Post not found with {}'.format(pk)}, status=404)
        post.delete()
        return Response({'message': 'Successfully deleted the post !'}, status=204)


@csrf_exempt
def posts(request):
    if request.method == 'GET':
        queryset = Post.objects.all()
        serializer = PostSerializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        parser = JSONParser()
        data = parser.parse(request)
        post = PostSerializer(data=data)
        if post.is_valid():
            post.save()
            return JsonResponse(post.data, status=201)
        return JsonResponse(post.errors, status=400)

@csrf_exempt
def post_detail(request, pk):
    try:
        # we cant use get_object_or_404 as ite returns 404 page as this is api we need to send a response
        post = Post.objects.get(pk=pk)
    except ObjectDoesNotExist:
        return JsonResponse({'error': 'Post not found with {}'.format(pk)}, status=404)
    if request.method == 'GET':
        post = PostSerializer(post)
        return JsonResponse(post.data)
    elif request.method == 'PUT':
        parser = JSONParser()
        data = parser.parse(request)
        post = PostSerializer(post, data=data)
        if post.is_valid():
            post.save()
            return JsonResponse(post.data)
        return JsonResponse(post.errors, status=400)
    elif request.method == 'DELETE':
        post.delete()
        return JsonResponse({'message': 'Successfully deleted the post !'}, status=204)

class LoginApiView(APIView):
    def post(self, request):
        data = LoginSerializer(data=request.data)
        data.is_valid(raise_exception=True)
        user = data.validated_data['user']
        login(request, user)
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})



class LogoutApiView(APIView):
    authentication_classes = (TokenAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)
    def post(self, request):
        request.user.auth_token.delete()
        logout(request)
        return Response(status=204)
# In headers
#Authorization Token 6bece4f19c201a92bd54c2ac738ceaa3a9c04cb0
# X-CSRFToken 8o8Pg86esDvh5vd7v9Pa0i57aJQHGZqaDMejTFfaL2FUj2JckHTrnxLLyNKasB8q