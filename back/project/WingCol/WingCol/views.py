from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *


@api_view(['GET'])
def get_all_users(request):
    users = NormalUser.objects.filter(activo=True)
    serializer = UserSerializer(users, many = True)
    return Response(serializer.data)

@api_view(['GET'])
def get_user(request, id):
    try:
        user = NormalUser.objects.get(user_id=id, activo=True)
        serializer = UserSerializer(user, many=False)
        return Response(serializer.data)
    except NormalUser.DoesNotExist:
        return Response({"error": "User does not exist"}, status=status.HTTP_404_NOT_FOUND)
    

@api_view(['POST'])
def create_client(request):
    user_serializer = UserSerializer(data=request.data)
    if user_serializer.is_valid():
        new_user = user_serializer.save()
        client_data = request.data.copy()
        client_data['user_id'] = new_user.user_id
        client_serializer = ClientSerializer(data=client_data)
        if client_serializer.is_valid():
            client_serializer.save()
            return Response(client_serializer.data, status=status.HTTP_201_CREATED)
        return Response(client_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_client(request):
    try:
        user = NormalUser.objects.get(user_id=request.data['user_id'])
        client = Cliente.objects.get(user_id=request.data['user_id'])
        user_serializer = UserSerializer(user, data=request.data)
        client_serializer = ClientSerializer(client, data=request.data)

        if user_serializer.is_valid() and client_serializer.is_valid():
            user_serializer.save()
            client_serializer.save()
            return Response(client_serializer.data, status=status.HTTP_202_ACCEPTED)
        
        return Response({
            "user_errors": user_serializer.errors,
            "client_errors": client_serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    except NormalUser.DoesNotExist:
        return Response({"error": "Usuario no existente"}, status=status.HTTP_404_NOT_FOUND)
    except Cliente.DoesNotExist:
        return Response({"error": "Cliente no existente"}, status=status.HTTP_404_NOT_FOUND)
    
@api_view(['PUT'])
def delete_client(request):
    try:
        user = NormalUser.objects.get(user_id=request.data['user_id'])
        client = Cliente.objects.get(user_id=request.data['user_id'])
        
        user.soft_delete()
        client.soft_delete()

        return Response({"message": "Cliente borrado correctamente."}, status=status.HTTP_200_OK)

    except NormalUser.DoesNotExist:
        return Response({"error": "Usuario no existente"}, status=status.HTTP_404_NOT_FOUND)
    except Cliente.DoesNotExist:
        return Response({"error": "Cliente no existente"}, status=status.HTTP_404_NOT_FOUND)
    
@api_view(['POST'])
def create_admin(request):
    user_serializer = UserSerializer(data=request.data)
    if user_serializer.is_valid():
        new_user = user_serializer.save()
        admin_data = request.data.copy()
        admin_data['user_id'] = new_user.user_id
        admin_serializer = AdministradorSerializer(data=admin_data)
        if admin_serializer.is_valid():
            admin_serializer.save()
            return Response(admin_serializer.data, status=status.HTTP_201_CREATED)
        return Response(admin_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_admin(request):
    try:
        user = NormalUser.objects.get(user_id=request.data['user_id'])
        admin = Administrador.objects.get(user_id=request.data['user_id'])
        user_serializer = UserSerializer(user, data=request.data)
        admin_serializer = AdministradorSerializer(admin, data=request.data)
        
        if user_serializer.is_valid() and admin_serializer.is_valid():
            user_serializer.save()
            admin_serializer.save()
            return Response(admin_serializer.data, status=status.HTTP_202_ACCEPTED)
        
        return Response({
            "user_errors": user_serializer.errors,
            "client_errors": admin_serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    except NormalUser.DoesNotExist:
        return Response({"error": "Usuario no existente"}, status=status.HTTP_404_NOT_FOUND)
    except Administrador.DoesNotExist:
        return Response({"error": "Cliente no existente"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT'])
def delete_admin(request):
    try:
        user = NormalUser.objects.get(user_id=request.data['user_id'])
        admin = Administrador.objects.get(user_id=request.data['user_id'])
        
        user.soft_delete()
        admin.soft_delete()

        return Response({"message": "Administrador borrado correctamente."}, status=status.HTTP_200_OK)

    except NormalUser.DoesNotExist:
        return Response({"error": "Usuario no existente"}, status=status.HTTP_404_NOT_FOUND)
    except Administrador.DoesNotExist:
        return Response({"error": "Administrador no existente"}, status=status.HTTP_404_NOT_FOUND)