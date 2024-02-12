from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('pastoral_team', views.pastoral, name="pastoral_team"),
    path('staff_and_council', views.staff, name="staff_and_council"),
    path('beliefs', views.beliefs, name="beliefs"),
    path('mission_vision_values', views.mission, name="mission_vision_values"),
    path('meetings', views.meetings, name="meetings"),
    path('new', views.new, name='new'),
    path('what_to_expect', views.expect, name='what_to_expect'),
    path('news', views.news, name="news"),
    path('contact', views.contact, name="contact"),
    path('next_steps', views.next_steps, name="next_steps"),
    path('groups', views.groups, name="groups"),
    path('volunteer', views.volunteer, name="volunteer"),
    path('prayer', views.prayer, name="prayer"),
    path('give', views.give, name="give"),
]
