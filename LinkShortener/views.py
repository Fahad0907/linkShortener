from urllib import response
from django.shortcuts import render
from .serializers import LinkSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Link
from datetime import datetime, timedelta
import pyshorteners
# Create your views here.
def makeUrlInvalide(user):
    query = Link.objects.filter(user=user,expired_date__lt=datetime.now(),valid = True)
    for i in query:
       
        url = i.shorten_url
        url_toList = []
        url_toList[:0] = url
        url_toList[8] = 'p'
        url = ''.join(url_toList)
        i.shorten_url = url
        i.valid = False
        i.save()
            
            
    
class LinkList(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = LinkSerializer(data=request.data)
        if serializer.is_valid():
            url = pyshorteners.Shortener().tinyurl.short(serializer.data['main_url'])
            print(datetime.now())
            link = Link.objects.create(user=request.user,main_url=serializer.data['main_url'],shorten_url=url,expired_date=serializer.data['expired_date'])
            link.save()
            return Response({"short url": url},status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def get(self,request):
        try:
            makeUrlInvalide(request.user)
            query = Link.objects.filter(user=request.user).order_by('created_at')
            serializer = LinkSerializer(query, many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    

    