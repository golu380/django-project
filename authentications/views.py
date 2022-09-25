
from django.shortcuts import render
from .user_auth_serializer import *
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.hashers import make_password,check_password
from rest_framework import status
# Create your views here.

def get_tokens_for_user(user):
  refresh = RefreshToken.for_user(user)
  return {
      'refresh': str(refresh),
      'access': str(refresh.access_token),
  }

class newuserRegistration():
    def post(self,request, format=None):
        password = request.data['password']
        length_pass = len(password)
        cpassword = request.data['Cpassword']
        email = request.data['email']

        if(length_pass<6):
            raise serializers.ValidationError("password must be greater then 6")
        user = newuser.objects.filter(email = email)
        if(user):
            raise serializers.ValidationError("User already exists")
        
        if(password != cpassword):
            raise serializers.ValidationError("Password not match")
        encryptpass = make_password(password)
        print(encryptpass)
        request.data._mutable = True  # for change in serializer data
        request.data.update({'password':encryptpass})

        serializers = newuserregisterSerializer(data = request.data)
        print(serializers)
        
        if(serializers.is_valid(raise_exception=True)):
            data = serializers.save()

            token = get_tokens_for_user(data)
            return Response({'token':token, 'msg':'Registration Successful'}, status=status.HTTP_201_CREATED)


