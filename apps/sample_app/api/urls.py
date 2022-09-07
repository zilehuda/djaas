from django.urls import path
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)


from apps.sample_app.api.views import (
    AuthenticatedOnlyAPIView,
    PublicOnlyAPIView,
    SubscribedOnlyAPIView,
)

urlpatterns = [
    path("subscribed-only/", SubscribedOnlyAPIView.as_view(), name="subscribed_only"),
    path(
        "authenticated-only/",
        AuthenticatedOnlyAPIView.as_view(),
        name="authenticated_only",
    ),
    path("public-only/", PublicOnlyAPIView.as_view(), name="public_only"),
]
