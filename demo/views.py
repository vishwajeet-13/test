from django.shortcuts import render
from .models import Demo
from .serializers import DemoSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class DemoView(APIView):
    def post(self,request):
        serializer = DemoSerializer(data=request.data)
        if serializer.is_valid():
            instance = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)