from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='profile')
    description = models.CharField(max_length=256, default='')
    city = models.CharField(max_length = 32,default='')
    website = models.URLField(default='')
    phone = models.CharField(max_length=10, validators=[MinLengthValidator(10)])
