from django.urls import path
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)


from apps.authentications.views import LoginAPIView, RegisterAPIView

urlpatterns = [
    path("register/", RegisterAPIView.as_view(), name="register"),
    path("login/", LoginAPIView.as_view(), name="login"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
