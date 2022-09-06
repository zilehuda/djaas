from django.urls import path
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)


from apps.authentications.api.views import LoginAPIView, RegisterAPIView

urlpatterns = [
    path("register/", RegisterAPIView.as_view(), name="register_api"),
    path("login/", LoginAPIView.as_view(), name="login_api"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
