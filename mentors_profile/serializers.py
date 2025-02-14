from rest_framework import serializers
from .models import Mentors, User

class MentorsSerializer(serializers.ModelSerializer):
    
    user_id = serializers.IntegerField(write_only = True)
    
    class Meta:
        model = Mentors
        fields = ['id','user','user_id','expertise',
                  'availability','hourly_rate', 'rating', 'created_at']
        
    def create(self, validated_data):
        user_id = validated_data.pop('user_id')
        user = User.objects.get(id = user_id)
        mentor = Mentors.objects.create(user = user, **validated_data)
        return mentor