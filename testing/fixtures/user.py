from django.contrib.auth.models import User
import pytest

@pytest.fixture
def new_user(request):
    user = User(email='test@test.com', username='test')
    user.set_password('test1231234')
    user.save()
    return user