from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import StaffProfile, PastoralProfile

# Home App is designed to run and manage static pages creating the base website


def home(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())


def about(request):
    template = loader.get_template('about.html')
    return HttpResponse(template.render())


def pastoral(request):
    pastoral_staff = PastoralProfile.objects.all().values()
    template = loader.get_template('pastoral_team.html')
    context = {
        'pastoral_staff': pastoral_staff,
    }
    return HttpResponse(template.render(context, request))


def staff(request):
    staff_team = StaffProfile.objects.all().values()
    template = loader.get_template('staff_and_council.html')
    context = {
        'staff_team': staff_team,
    }
    return HttpResponse(template.render(context, request))


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
