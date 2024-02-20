from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser

from .models import StaffProfile, PastoralProfile, FirstTimer
from .serializers import StaffSerializer, PastorSerializer, FirstTimerSerializer

# Home App is designed to run and manage static pages creating the base website


@api_view(['GET'])
def getStaffProfile(request):
    staffprofile = StaffProfile.objects.all()
    serializer = StaffSerializer(staffprofile, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def postStaffProfile(request):
    serializer = StaffSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)


@api_view(['GET'])
def getPastorProfile(request):
    pastorprofile = PastoralProfile.objects.all()
    serializer = PastorSerializer(pastorprofile, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def postPastorProfile(request):
    serializer = PastorSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)


@api_view(['GET'])
def getFirstTimerProfile(request):
    firsttimerprofile = FirstTimer.objects.all()
    serializer = FirstTimerSerializer(firsttimerprofile, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def postFirstTimerProfile(request):
    serializer = FirstTimerSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)


def home(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())


def about(request):
    template = loader.get_template('about.html')
    return HttpResponse(template.render())


@csrf_exempt
def pastoral(request):
    if request.method == 'GET':
        pastoral_staff = PastoralProfile.objects.all()
        serializer = PastorSerializer(pastoral_staff, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PastorSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
    """template = loader.get_template('pastoral_team.html')
    context = {
        'pastoral_staff': pastoral_staff,
    }
    return HttpResponse(template.render(context, request))"""


@csrf_exempt
def pastor_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        pastoral_staff = PastoralProfile.objects.get(pk=pk)
    except PastoralProfile.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = PastorSerializer(pastoral_staff)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = PastorSerializer(pastoral_staff, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        pastoral_staff.delete()
        return HttpResponse(status=204)


def staff(request):
    if request.method == 'GET':
        staff = StaffProfile.objects.all()
        serializer = StaffSerializer(staff, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = StaffSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    """staff_team = StaffProfile.objects.all().values()
    template = loader.get_template('staff_and_council.html')
    context = {
        'staff_team': staff_team,
    }
    return HttpResponse(template.render(context, request))"""


@csrf_exempt
def staff_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        staff = StaffProfile.objects.get(pk=pk)
    except StaffProfile.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = StaffSerializer(staff)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = PastorSerializer(staff, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        staff.delete()
        return HttpResponse(status=204)


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
