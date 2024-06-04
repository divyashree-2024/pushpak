from django.urls import path
from .viewsets import RegisterUserViewSet, UserViewSet, UserAddressViewSet


urlpatterns = [
    path("create-user/", RegisterUserViewSet.as_view({"post": "create_user"})),
    path("login/", RegisterUserViewSet.as_view({"post": "login"})),
    path("logout/", UserViewSet.as_view({"get": "logout"})),
    path("update/", UserViewSet.as_view({"patch": "update_profile"})),
    path("address/", UserAddressViewSet.as_view({"post": "create"}))
]