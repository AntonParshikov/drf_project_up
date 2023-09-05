from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView

from users.models import User
from users.serializers import UserListSerializer, UserSerializer


class UserListView(ListAPIView):
    serializer_class = UserListSerializer
    queryset = User.objects.all()


class UserCreateView(CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
