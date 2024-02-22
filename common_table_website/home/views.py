from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from rest_framework import generics
from .models import StaffProfile, PastoralProfile, FirstTimer
from .serializers import StaffSerializer, PastorSerializer, FirstTimerSerializer

# Home App is designed to run and manage static pages creating the base website


def home(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())


def about(request):
    template = loader.get_template('about.html')
    return HttpResponse(template.render())


class PastoralList(generics.ListCreateAPIView):
    queryset = PastoralProfile.objects.all()
    serializer_class = PastorSerializer

def pastoral_team(request):
    template = loader.get_template('pastoral_team.html')
    return HttpResponse(template.render())


class PastorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PastoralProfile.objects.all()
    serializer_class = PastorSerializer


class StaffList(generics.ListCreateAPIView):
    queryset = StaffProfile.objects.all()
    serializer_class = StaffSerializer

def staff(request):
    template = loader.get_template('staff_and_council.html')

    return HttpResponse(template.render())


class StaffDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = StaffProfile.objects.all()
    serializer_class = StaffSerializer


def beliefs(request):
    template = loader.get_template('beliefs.html')
    return HttpResponse(template.render())


def mission(request):
    template = loader.get_template('mission_vision_values.html')
    return HttpResponse(template.render())


def meetings(request):
    template = loader.get_template('meetings.html')
    return HttpResponse(template.render())


def new(request):
    template = loader.get_template('new.html')
    return HttpResponse(template.render())


def expect(request):
    template = loader.get_template('what_to_expect.html')
    return HttpResponse(template.render())


def news(request):
    template = loader.get_template('news.html')
    return HttpResponse(template.render())


def contact(request):
    template = loader.get_template('contact.html')
    return HttpResponse(template.render())


def next_steps(request):
    template = loader.get_template('next_steps.html')
    return HttpResponse(template.render())


def groups(request):
    template = loader.get_template('groups.html')
    return HttpResponse(template.render())


def volunteer(request):
    template = loader.get_template('volunteer.html')
    return HttpResponse(template.render())


def prayer(request):
    template = loader.get_template('prayer.html')
    return HttpResponse(template.render())


def give(request):
    template = loader.get_template('give.html')
    return HttpResponse(template.render())


def partnership(request):
    template = loader.get_template('partnership.html')
    return HttpResponse(template.render())
