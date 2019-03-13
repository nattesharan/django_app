from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
from django.db.models.signals import post_save
# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='profile')
    description = models.CharField(max_length=256, default='')
    city = models.CharField(max_length = 32,default='')
    website = models.URLField(default='')
    phone = models.CharField(max_length=10, validators=[MinLengthValidator(10)])

    def __str__(self):
        return self.user.username
        
def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])


post_save.connect(create_profile, sender=User)