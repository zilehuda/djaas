import pytest
from rest_framework.reverse import reverse


def test_login_with_correct_cred(user, secret_pwd, api_client):
    data = {
        "username": user.username,
        "password": secret_pwd,
    }
    url = reverse("login_api")
    response = api_client.post(url, data)
    json_resp = response.json()
    assert response.status_code == 200
    assert json_resp["success"] == True


def test_login_with_incorrect_cred(user, api_client):
    data = {
        "username": user.username,
        "passwordd": "invalid_cred",
    }
    url = reverse("login_api")
    response = api_client.post(url, data)
    json_resp = response.json()
    assert response.status_code == 400
    assert json_resp["success"] == False


def test_login_with_validation_error(user, secret_pwd, api_client):
    data = {
        "username": user.username,
        "passwordd": secret_pwd,
    }
    url = reverse("login_api")
    response = api_client.post(url, data)
    json_resp = response.json()
    assert response.status_code == 400
    assert json_resp["success"] == False
    assert json_resp["is_validation_error"] == True


def test_register(api_client):
    data = {
        "username": "bob",
        "email": "bob@django.com",
        "password": "secret_pwd",
        "confirm_password": "secret_pwd",
    }
    url = reverse("register_api")
    response = api_client.post(url, data)
    json_resp = response.json()
    assert response.status_code == 200
    assert json_resp["success"] == True


def test_test_register_with_validation_error(api_client):
    data = {
        "username": "bob",
        "wrong_email_key": "bob@django.com",
        "password": "secret_pwd",
        "confirm_password": "secret_pwd",
    }
    url = reverse("register_api")
    response = api_client.post(url, data)
    json_resp = response.json()
    assert response.status_code == 400
    assert json_resp["success"] == False
    assert json_resp["is_validation_error"] == True


def test_test_register_confirm_pwd_mismatch(api_client):
    data = {
        "username": "bob",
        "email": "bob@django.com",
        "password": "secret_pwd",
        "confirm_password": "invalid_pwd",
    }
    url = reverse("register_api")
    response = api_client.post(url, data)
    json_resp = response.json()
    assert response.status_code == 400
    assert json_resp["success"] == False
    assert json_resp["is_validation_error"] == True
