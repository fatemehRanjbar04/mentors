from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from .models import Mentors
from .serializers import MentorsSerializer 

class MentorsList(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        mentor = Mentors.objects.all()
        serializer = MentorsSerializer(mentor, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        user = request.user
        data = request.data
        serializer = MentorsSerializer(data = data)
        if serializer.is_valid():
            serializer.save(user = user)
            return Response({
                                "success": True,
                                "message": "Mentor profile created successfully.",
                                "mentor_id": serializer.instance.id},
                            status=status.HTTP_201_CREATED)
            
        return Response({"success":False, "message":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    
class MentorDetail(APIView):
    permission_classes = [IsAuthenticated]
    
    def get_object(self, mentor_id):
        try:
            mentor = Mentors.objects.get(id = mentor_id)
        except Mentors.DoesNotExist:
            return Response({"success": False, 
                             "message":"Mentor not found."}, status = status.HTTP_404_NOT_FOUND)
        return mentor
    
    
    def patch(self, request, mentor_id):
        mentor = self.get_object(mentor_id)
        serializer = MentorsSerializer(mentor, data = request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response({"success": True,
                            "message": "Mentor profile updated successfully.",})
        return Response(serializer.errors)
    
    
    def delete(self, request, mentor_id):
        mentor = self.get_object(mentor_id)
        mentor.delete()
        return Response({"success": True, "message": "Mentor profile deleted Successfully."}, status = status.HTTP_204_NO_CONTENT)