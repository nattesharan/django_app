from rest_framework import viewsets
from django.contrib.auth.models import User
from api.serializers import UserSerializer

class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer