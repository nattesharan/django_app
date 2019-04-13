from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
from django.db.models.signals import post_save

class UserProfileManager(models.Manager):
    def get_queryset(self):
        return super(UserProfileManager, self).get_queryset().filter(user__is_superuser=True)

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='profile')
    description = models.CharField(max_length=256, default='')
    city = models.CharField(max_length = 32,default='')
    website = models.URLField(default='')
    phone = models.CharField(max_length=10, validators=[MinLengthValidator(10)])
    image = models.ImageField(upload_to='profile_images', blank=True)
    friends = models.ManyToManyField(User, related_name='friends')
    objects = models.Manager()
    super_user_profile = UserProfileManager()
    def __str__(self):
        return self.user.username
    
    @classmethod
    def add_friend(cls, user, friend):
        user_profile = cls.objects.get(user=user)
        user_profile.friends.add(friend)

def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])


post_save.connect(create_profile, sender=User)