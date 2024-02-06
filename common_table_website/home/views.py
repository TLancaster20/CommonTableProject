from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Home App is designed to run and manage static pages creating the base website


def home(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())


def about(request):
    template = loader.get_template('about.html')
    return HttpResponse(template.render())


def pastoral(request):
    template = loader.get_template('pastoral_team.html')
    return HttpResponse(template.render())


def staff(request):
    template = loader.get_template('staff_and_council.html')
    return HttpResponse(template.render())


def beliefs(request):
    template = loader.get_template('beliefs.html')
    return HttpResponse(template.render())


def mission(request):
    template = loader.get_template('mission_vision_values.html')
    return HttpResponse(template.render())


def find(request):
    template = loader.get_template('find.html')
    return HttpResponse(template.render())


def community(request):
    template = loader.get_template('community.html')
    return HttpResponse(template.render())
