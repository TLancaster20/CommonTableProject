from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('find', views.find, name="find"),
    path('community', views.community, name="community"),
]
