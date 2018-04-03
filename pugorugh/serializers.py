from django.contrib.auth import get_user_model

from rest_framework import serializers

from . import models


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = get_user_model().objects.create(
            username=validated_data['username'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model = get_user_model()


class DogSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'name',
            'image_filename',
            'breed',
            'age',
            'gender',
            'size',
            'sterilized',
        )

        model = models.Dog


class UserDogSerializer(serializers.ModelSerializer):
    extra_kwargs = {
        'user': {'write_only': True}
    }

    class Meta:
        fields = (
            'dog',
            'status',
        )

        model = models.UserDog


class UserPrefSerializer(serializers.ModelSerializer):
    extra_kwargs = {
        'user': {'write_only': True}
    }

    class Meta:
        fields = (
            'age',
            'gender',
            'size',
            'sterilized',
        )

        model = models.UserPref
