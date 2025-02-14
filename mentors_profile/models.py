from django.db import models
from django.contrib.auth.models import User

class Mentors(models.Model):
    
    user = models.OneToOneField(User, on_delete= models.CASCADE)
    expertise = models.JSONField(null=False)
    availability = models.JSONField(null=False)
    hourly_rate = models.DecimalField(max_digits = 10,decimal_places = 2)
    rating = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user.username
