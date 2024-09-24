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
    if user_serializer.is_valid():
        new_user = user_serializer.save()
        client_data = request.data.copy()
        client_data['user_id'] = new_user
        client_serializer = ClientSerializer(data=client_data)
        # print(client_serializer)
        if client_serializer.is_valid():
            client_serializer.save()
            return Response(client_serializer.data, status=status.HTTP_201_CREATED)
        return Response(client_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)