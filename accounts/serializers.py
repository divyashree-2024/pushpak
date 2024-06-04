from rest_framework import serializers
from .models import UserProfile, UserAddress, User
from django.contrib.auth.hashers import make_password


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "first_name", "last_name", "email")


class UserSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    username = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def to_internal_value(self, data):
        data = super().to_internal_value(data)
        password = data.get("password", "")
        password = make_password(password)
        data["password"] = password
        return data

    def create(self, validated_data):
        return User.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance


class UserProfileSerializer(serializers.Serializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    date_of_birth = serializers.DateField()
    college = serializers.CharField()
    mobile = serializers.CharField()

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data.pop("user", None)
        return data
    
    def create(self, validated_data):
        return UserProfile.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance


class UserAddressSerializer(serializers.Serializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    address_name = serializers.CharField()
    address_line_1 = serializers.CharField()
    address_line_2 = serializers.CharField()
    address_city = serializers.CharField()
    address_state = serializers.CharField()
    address_country = serializers.CharField()
    address_pincode = serializers.CharField()
    
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data.pop("user", None)
        return data
    
    def create(self, validated_data):
        return UserAddress.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance