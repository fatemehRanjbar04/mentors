from django.urls import path
from .views import MentorsList, MentorDetail

urlpatterns = [
    path('', MentorsList.as_view(), name = 'mentors-list'),
    path('<int:mentor_id>/', MentorDetail.as_view(), name = 'mentor-profile-detail')
]