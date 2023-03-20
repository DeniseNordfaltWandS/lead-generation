from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from .models import User
from .serializers import UserSerializer

class UserCreateView(CreateAPIView):
    queryset = User.objects.none()
    serializer_class = UserSerializer