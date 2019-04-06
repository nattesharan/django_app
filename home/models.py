from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    post = models.CharField(max_length=500)
    user = models.ForeignKey(User, related_name='posts')
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.post