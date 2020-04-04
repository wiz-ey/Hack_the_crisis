from django.shortcuts import render
from django.http import Http404
from .models import Person, DailyLog, Area
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import RequestSerializer
import datetime

risk_list = []

def parse_as_area(location):
    lat_int = int(location.latitude)
    lon_int = int(location.longitude)
    lat_int_low = lat_int - (lat_int % 10)
    lat_int_high = lat_int_low + 10
    lon_int_low = lon_int - (lon_int % 10)
    lon_int_high = lon_int_low + 10
    area = Area.objects.get_or_create(min_lat = lat_int_low, max_lat = lat_int_high, min_lon = lon_int_low, max_lon = lon_int_high)
    return area


def date_parser(date_time):
    return date_time.split()[0]

def time_parser(date_time):
    return (date_time.split()[1]).split('-')[0]


# Create your views here.
class UpdateLogs(APIView):
    def get_person(self, pk):
        try:
            return Person.objects.get(pk=pk)
        except Person.DoesNotExist:
            raise Http404
    def get_daily_log(self, date, area):
        return DailyLog.objects.get_or_create(date=date, area = area)

    def post(self, request, pk, format=None):
        serialiizer = RequestSerializer(data=request.data)
        if serialiizer.is_valid():
            area = parse_as_area(request.data[location])
            date = date_parser(request.data[time_stamp])
            time = time_parser(request.data[time_stamp])
            person = self.get_person(pk)
            person.location_log.append((area, time, date))
            person.save()
            daily_log = self.get_daily_log(date, area)
            daily_log.log[time].append(request.data[name])

def risk_marker(request, pk):

    try:
        person = Person.objects.get(pk=pk)
    except Person.DoesNotExist:
        raise Http404

    for i in range(len(person.location_log)):
        area = Area.objects.get(person.location_log[i][0])
        daily_log = area.DailyLog(date=person.location_log[i][2])
        risk_list.append(daily_log.log[person.location_log[i][1]] - person.name)
