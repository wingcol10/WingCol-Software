from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *


@api_view(['GET'])
def get_users(request):
    users = NormalUser.objects.all()
    serializer = UserSerializer(users, many = True)
    return Response(serializer.data)

@api_view(['POST'])
def create_client(request):
    user_serializer = UserSerializer(data=request.data)
    client_serializer = ClientSerializer(data=request.data)
    if user_serializer.is_valid() and client_serializer.is_valid():
        user_serializer.save()
        client_serializer.save()
        return Response(user_serializer, client_serializer, status=status.HTTP_201_CREATED)
    return Response(user_serializer, client_serializer, status=status.HTTP_400_BAD_REQUEST)