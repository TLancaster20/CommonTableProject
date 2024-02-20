from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import StaffProfile, PastoralProfile, FirstTimer
from .serializers import StaffSerializer, PastorSerializer, FirstTimerSerializer

# Home App is designed to run and manage static pages creating the base website


def home(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())


def about(request):
    template = loader.get_template('about.html')
    return HttpResponse(template.render())


@api_view(['GET', 'POST'])
def pastoral(request):
    if request.method == 'GET':
        pastoral_staff = PastoralProfile.objects.all()
        serializer = PastorSerializer(pastoral_staff, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = PastorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    """template = loader.get_template('pastoral_team.html')
    context = {
        'pastoral_staff': pastoral_staff,
    }
    return HttpResponse(template.render(context, request))"""


@api_view(['GET', 'PUT', 'DELETE'])
def pastor_detail(request, pk):
    try:
        pastoral_staff = PastoralProfile.objects.get(pk=pk)
    except PastoralProfile.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PastorSerializer(pastoral_staff)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PastorSerializer(pastoral_staff, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        pastoral_staff.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def staff(request):
    if request.method == 'GET':
        staff_members = StaffProfile.objects.all()
        serializer = StaffSerializer(staff_members, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = StaffSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    """staff_team = StaffProfile.objects.all().values()
    template = loader.get_template('staff_and_council.html')
    context = {
        'staff_team': staff_team,
    }
    return HttpResponse(template.render(context, request))"""


@api_view(['GET', 'PUT', 'DELETE'])
def staff_detail(request, pk):
    try:
        staff_member = StaffProfile.objects.get(pk=pk)
    except StaffProfile.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = StaffSerializer(staff_member)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PastorSerializer(staff, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        staff_member.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


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
