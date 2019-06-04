import pytest
from django.contrib.auth.models import User
from django.test import TestCase
@pytest.mark.django_db
def test_create_user():
    user = User(email='test@test.com', username='test')
    user.set_password('test1231234')
    user.save()
    created_user = User.objects.get(pk=user.pk)
    assert created_user

@pytest.mark.django_db
class TestUser:
    def test_create_user(self):
        user = User(email='test@test.com', username='test')
        user.set_password('test1231234')
        user.save()
        created_user = User.objects.get(pk=user.pk)
        assert created_user

@pytest.mark.django_db
class TestUserWithSetup(TestCase):
    @classmethod
    def setUpClass(cls):
        super(TestUserWithSetup, cls).setUpClass()
        cls.user = User(email='test@test.com', username='test')
        cls.user.set_password('test1231234')
        cls.user.save()

    def test_create_user(self):
        created_user = User.objects.get(pk=self.user.pk)
        assert created_user

@pytest.mark.django_db
class TestUserWithFixture:
    def test_create_user(self, new_user):
        created_user = User.objects.get(pk=new_user.pk)
        assert created_user
        assert False
#--reuse-db - reuse the testing database between test runs
# --create-db - force re creation of the test database
# --nomigrations will disable Django migrations and create the database by inspecting all models.