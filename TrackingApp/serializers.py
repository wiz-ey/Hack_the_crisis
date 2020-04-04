from rest_framework import serializers
from drf_extra_fields.geo_fields import PointField

class RequestSerializer(serializers.Serializer):
    name = serializers.CharField(blank=False, max_length=256)
    time_stamp = serializers.DateTimeField()
    location = PointField()

    
