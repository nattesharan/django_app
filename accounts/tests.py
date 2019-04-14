from django.test import TestCase
from django.contrib.auth.models import User
from django.shortcuts import reverse
from django.test import Client

# Create your tests here.
class UserTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User(email='test@test.com', username='test')
        self.user.set_password('test1231234')
        self.user.save()
    
    def test_user_created(self):
        user = User.objects.get(pk=self.user.pk)
        assert user
    
    def test_client(self):
        response = self.client.get(reverse('accounts:login'))
        self.assertTrue(response.status_code == 200, 'It works')
# --keepdb in test will not drop the db check https://django-testing-docs.readthedocs.io/en/latest/views.html for more info