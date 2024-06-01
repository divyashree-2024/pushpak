from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from .serializers import UserProfileSerializer, UserAddressSerializer, UserSerializer, UserLoginSerializer
from .models import User, UserProfile, UserAddress
from django.contrib.auth.hashers import check_password
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class RegisterUserViewSet(ViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = ()
    permission_classes = ()

    def create_user(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)
        if not serializer.is_valid():
            return Response(data=serializer.errors, status=HTTP_400_BAD_REQUEST)
        
        serializer.save()
        return Response(data=serializer.data, status=HTTP_200_OK)

    def login(self, request):
        data = request.data
        serializer = UserLoginSerializer(data=data)
        if not serializer.is_valid():
            return Response(data=serializer.errors, status=HTTP_400_BAD_REQUEST)
        try:
            user = User.objects.get(username=data.get("username"))
        except User.DoesNotExist:
            return Response(data="Invalid Username", status=HTTP_400_BAD_REQUEST)
        if not user.check_password(data.get("password")):
            return Response(data="Invalid Password", status=HTTP_400_BAD_REQUEST)
    
        token, created = Token.objects.get_or_create(user=user)
        response_data = self.serializer_class(instance=user).data
        response_data["token"] = token.key
    
        return Response(data=response_data, status=HTTP_200_OK)
    
class UserViewSet(ViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


    def logout(self, request):
        user = request.user
        user.auth_token.delete()
        return Response(data={}, status=HTTP_200_OK)