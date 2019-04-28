from rest_framework import viewsets
from django.contrib.auth.models import User
from api.serializers import UserSerializer, PostSerializer
from home.models import Post
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

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
