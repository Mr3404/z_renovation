from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ParseError
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User

from .serializers import UserSerializer, UserRegisterSerializerWithToken, UserSerializerDetail


class UserDetailView(APIView):
    def get(self, request):
        user = User.objects.all()
        serializer = UserSerializerDetail(user, many=True)
        return Response(serializer.data)


# User Register View

class UserRegisterWithTokenView(APIView):

    def post(self, request):
        try:
            data = request.data
            user = User.objects.create(
                username=data["username"],
                first_name=data["first_name"],
                last_name=data["last_name"],
                is_staff=data["is_staff"],
                password=make_password(data["password"])
            )
            serializer = UserRegisterSerializerWithToken(user, many=False)
            return Response(serializer.data)
        except Exception as E:
            raise ParseError(E)