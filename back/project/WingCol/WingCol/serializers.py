from rest_framework import serializers
from .models import *

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model =  NormalUser
        fields = ['user_id', 'email', 'roles']