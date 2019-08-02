import graphene
from graphene_django.types import DjangoObjectType
from home.models import Post, User

class PostType(DjangoObjectType):
    class Meta:
        model = Post

class UserType(DjangoObjectType):
    class Meta:
        model = User

class Query(graphene.ObjectType):
    users = graphene.List(UserType)
    posts = graphene.List(PostType)
    user = graphene.Field(UserType, id=graphene.ID())
    post = graphene.Field(PostType,id=graphene.ID())

    def resolve_users(self, info, **kwargs):
        return User.objects.all()
    
    def resolve_posts(self, info, **kwargs):
        return Post.objects.all()
    
    def resolve_user(self, info, **kwargs):
        id = kwargs.get('id', None)
        if id:
            return User.objects.get(pk=id)
        return None
    
    def resolve_post(self, info, **kwargs):
        id = kwargs.get('id', None)
        if id:
            return Post.objects.get(pk=id)
        return None

class Mutation(graphene.ObjectType):
    add_post = graphene.Field(PostType, post=graphene.String(), user=graphene.ID())

    def resolve_add_post(self, info, **kwargs):
        post = kwargs.get('post')
        user_id = kwargs.get('user')
        user = User.objects.get(pk=user_id)
        return Post.objects.create(post=post, user=user)
schema = graphene.Schema(query=Query, mutation=Mutation)