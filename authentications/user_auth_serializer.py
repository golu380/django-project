from dataclasses import field
from unittest.util import _MAX_LENGTH
from rest_framework import serializers
from .models import *

class newuserregisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length = 255)
    Cpassword = serializers.CharField(max_length = 255,read_only=True)
    class Meta:
        model = newuser
        fields = ['email','name','password','Cpassword','phone']