from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt import authentication
from django.contrib.auth.models import User
from .models import Mentors
from .serializers import MentorsSerializer 

class MentorsList(APIView):
    def get(self, request):
        mentor = Mentors.objects.all()
        serializer = MentorsSerializer(mentor, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        data = request.data
        user_id = data.get('user_id')
        try:
            user = User.objects.get(id = user_id)
        except User.DoesNotExist:
            return Response({"success": False,"message": "Invalid user ID."}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = MentorsSerializer(data = data)
        if serializer.is_valid():
            serializer.save(user = user)
            return Response({
                                "success": True,
                                "message": "Mentor profile created successfully.",
                                "mentor_id": serializer.instance.id},
                            status=status.HTTP_201_CREATED)
            
        return Response({"success":False, "message":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)