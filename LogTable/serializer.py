from rest_framework import serializers
from .models import *

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model=Roles
        fields=('role','id')

        
class logSerializer(serializers.ModelSerializer):
    class Meta:
        model=LogsTable
        fields=('day','time_in','time_out')

class UserSerializer(serializers.ModelSerializer):
    logs=logSerializer(many=True,read_only=True)
    role=RoleSerializer(many=True,read_only=True)
    class Meta:
        model=User
        fields=('id','uniqueid','firstName','lastName','email','phone','password','role','logs')
        depth=1