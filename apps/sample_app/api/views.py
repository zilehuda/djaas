from rest_framework.views import APIView
from rest_framework.response import Response
from utils.permissions import IsSubscriptionActive
from rest_framework.permissions import IsAuthenticated, AllowAny
from utils.response.resp import DjaasResponse


class SubscribedOnlyAPIView(APIView):
    permission_classes = (
        IsAuthenticated,
        IsSubscriptionActive,
    )

    def get(self, request):
        return Response(
            DjaasResponse.get_response(
                success=True, message="Thanks for your subscription."
            )
        )


class AuthenticatedOnlyAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        return Response(
            DjaasResponse.get_response(
                success=True, message=f"Welcome to djaas {request.user.username}"
            )
        )


class PublicOnlyAPIView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        return Response(
            DjaasResponse.get_response(success=True, message="Hey everyone...")
        )
