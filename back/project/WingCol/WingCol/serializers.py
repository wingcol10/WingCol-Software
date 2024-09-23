from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model =  NormalUser
        fields = ['user_id', 'email', 'roles', 'password']

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['user_id', 'nombre', 'segundo_nombre', 
                  'tipo_documento', 'fecha_nacimiento', 
                  'genero', 'telefono', 'direccion', 'direccion_facturacion']