from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),

    path('pastoral_team', views.pastoral_team, name="pastoral_team"),
    path('pastoral_list', views.PastoralList.as_view()),
    path('pastoral_list/<int:pk>/', views.PastorDetail.as_view()),

    path('staff_and_council', views.staff, name="staff_and_council"),
    path('staff_list', views.StaffList.as_view()),
    path('staff_list/<int:pk>/', views.StaffDetail.as_view()),

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
    path('partnership', views.partnership, name="partnership"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
