import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from apps.users.factories import UserFactory


@pytest.fixture(autouse=True)
def enable_db_access(db):
    """This method (fixture) will enable db access globally for all tests"""
    pass


@pytest.fixture
def user():
    return UserFactory.create(username="bob", password="secret_pwd")


@pytest.fixture
def secret_pwd():
    return "secret_pwd"


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def user_api_client(api_client, user):
    api_client.force_authenticate(user=user)
    yield api_client
    api_client.force_authenticate(user=None)
