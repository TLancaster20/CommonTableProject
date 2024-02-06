from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('find', views.find, name="find"),
    path('community', views.community, name="community"),
    path('pastoral_team', views.pastoral, name="pastoral_team"),
    path('staff_and_council', views.staff, name="staff_and_council"),
    path('beliefs', views.beliefs, name="beliefs"),
    path('mission_vision_values', views.mission, names="mission_vision_values")
]
