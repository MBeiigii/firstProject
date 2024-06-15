# myapp/serializers.py
from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name','factory']


class TextSerializer(serializers.Serializer):
    text = serializers.CharField(max_length=1000)




