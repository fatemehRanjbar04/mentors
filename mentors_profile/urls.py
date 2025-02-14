from django.urls import path
from .views import MentorsList

urlpatterns = [
    path('', MentorsList.as_view(), name = 'mentors-list'),
]