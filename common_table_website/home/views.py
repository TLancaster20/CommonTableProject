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

def find(request):
    template = loader.get_template('find.html')
    return HttpResponse(template.render())

def community(request):
    template = loader.get_template('community.html')
    return HttpResponse(template.render())
