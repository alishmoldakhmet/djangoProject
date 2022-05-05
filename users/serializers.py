from rest_framework import serializers
from sqlalchemy import false
from .models import User
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):


    class Meta:
        model = User
        fields = ("id","full_name","email","username")

        extra_kwargs = {
            "id": { "read_only" : True },
        }



class RegistrationSerializer(serializers.Serializer):
    full_name = serializers.CharField(max_length=100)
    image = serializers.ImageField(required=False)
    password = serializers.CharField(max_length=128,write_only=True)
    email = serializers.EmailField()
    username = serializers.CharField(max_length=150)


    # def isrefistered(self,validated_data):
        # instance = User.objects.create(**validated_data)
        # instance.set_password(validated_data.get('password'))
        # instance.save()
        # return instance


    # def useof(self,validated_data):
        # instance.save()
        # return instance


    def validate(self, data):
        data = super().validate(data)
        if data.get('email'):
            if User.objects.filter(email=data.get('email')).exists():
                raise serializers.ValidationError("Email уже существует!")
        return data


    # def useof(self,validated_data):
        # instance.save()
        # return instance
    def create(self,validated_data):
        instance = User.objects.create(**validated_data)
        instance.set_password(validated_data.get('password'))
        instance.save()
        return instance
