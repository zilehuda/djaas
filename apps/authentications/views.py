from apps.authentications.serializers import LoginSerializer, RegisterSerializer
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from utils.response.resp import DjaasResponse


class LoginAPIView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        data = request.data
        login_serializer = LoginSerializer(data=data)
        login_serializer.is_valid(raise_exception=True)

        return Response(
            DjaasResponse.get_response(
                data={
                    "token": login_serializer.validated_data,
                }
            )
        )


class RegisterAPIView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        data = request.data
        serializer = RegisterSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response("done")
