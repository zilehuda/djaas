import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient


@pytest.fixture(autouse=True)
def enable_db_access(db):
    """This method (fixture) will enable db access globally for all tests"""
    pass


@pytest.fixture
def user():
    return User.objects.create(username="bob")


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def user_api_client(api_client, user):
    api_client.force_authenticate(user=user)
    yield api_client
    api_client.force_authenticate(user=None)
