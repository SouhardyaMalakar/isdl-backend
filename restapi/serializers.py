from asyncore import write
from tkinter import N
from rest_framework import serializers

from restapi.models import User

# class HallSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=Hall
#         fields='__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields='__all__'
    

class USerLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','email','password','name']
        extra_kwargs={
            'password':{'write_only':True}
        }
    def create(self,validated_data):
        password=validated_data.pop('password',None)
        instance=self.Meta.model(**validated_data)
        if password!=None:
            instance.set_password(password)
        instance.save()
        return instance