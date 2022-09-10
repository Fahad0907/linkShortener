from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.contrib import auth
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserRegistrationSerializer
# Create your views here.

class Login(APIView):
    def post(self, request):
     
        username = request.data['username']
        password = request.data['password']
        user = auth.authenticate(username=username, password=password)
        print(user)
        if user is not None:
            auth.login(request, user)
            refresh = RefreshToken.for_user(user)
            return Response({'refresh': str(refresh),'access': str(refresh.access_token)},status=  status.HTTP_200_OK)
        else:
            return Response(status = status.HTTP_401_UNAUTHORIZED)
           

        
class Registration(APIView):
    def post(self, request):
        serializer = UserRegistrationSerializer(data = request.data)
        
        if serializer.is_valid():
            serializer.save()
            user = User.objects.get(username = serializer.data['username'])
            refresh = RefreshToken.for_user(user)
            return Response({'refresh': str(refresh),'access': str(refresh.access_token)},status=  status.HTTP_201_CREATED)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    
    
    
    
