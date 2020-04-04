from django.db import models
from picklefield.fields import PickledObjectField
# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=256)
    is_covid = models.BooleanField(default=False)
    is_at_risk = models.BooleanField(default=False)
    location_log = PickledObjectField()

class Area(models.Model):
    min_lat = models.IntegerField(max_length=50)
    max_lat = models.IntegerField(max_length=50)
    min_lon = models.IntegerField(max_length=50)
    max_lon = models.IntegerField(max_length=50)

class DailyLog(models.Model):
    area = models.ForeignKey(Area, on_delete=models.CASCADE)
    date = models.DateField()
    log = PickledObjectField()
